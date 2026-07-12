from typing import Type, TypeVar

from pydantic import BaseModel, ValidationError

from clients.llm.gemini_client import GeminiClient


T = TypeVar("T", bound=BaseModel)


class BaseAIService:
    """
    Base class for AI-powered services.
    """

    def __init__(self):
        self.gemini_client = GeminiClient()

    def generate_structured_output(
        self,
        prompt: str,
        response_model: Type[T],
    ) -> T:
        """
        Generate structured output using Gemini and validate it with Pydantic.
        """

        response = self.gemini_client.generate(prompt)

        try:
            return response_model.model_validate_json(response)

        except ValidationError as e:
            raise ValueError(
                f"Failed to parse Gemini response into "
                f"{response_model.__name__}."
            ) from e