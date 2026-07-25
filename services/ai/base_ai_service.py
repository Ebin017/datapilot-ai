from typing import Type, TypeVar

from pydantic import BaseModel, ValidationError

from clients.llm.gemini_client import GeminiClient
from clients.llm.ollama_client import OllamaClient

from config.settings import Settings

T = TypeVar("T", bound=BaseModel)


class BaseAIService:
    """
    Base class for AI-powered services.
    """

    def __init__(self):
        if Settings.LLM_PROVIDER == "ollama":
            self.client = OllamaClient()
        else:
            self.client = GeminiClient()

    def _clean_json_response(
        self,
        response: str,
    ) -> str:
        """
        Remove Markdown code fences from LLM responses.
        """

        response = response.strip()

        if response.startswith("```json"):
            response = response[len("```json"):].strip()

        elif response.startswith("```"):
            response = response[len("```"):].strip()

        if response.endswith("```"):
            response = response[:-3].strip()

        return response

    def generate_structured_output(
        self,
        prompt: str,
        response_model: Type[T],
    ) -> T:
        """
        Generate structured output using the configured LLM
        and validate it with Pydantic.
        """

        response = self.client.generate(prompt)

        response = self._clean_json_response(
            response,
        )

        try:
            return response_model.model_validate_json(
                response,
            )

        except ValidationError as e:
            raise ValueError(
                f"Failed to parse LLM response into "
                f"{response_model.__name__}."
            ) from e