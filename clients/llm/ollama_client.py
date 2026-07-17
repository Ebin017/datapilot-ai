import ollama

from config.settings import Settings


class OllamaClient:
    """
    Client for interacting with a local Ollama model.
    """

    def generate(
        self,
        prompt: str,
    ) -> str:

        response = ollama.chat(
            model=Settings.OLLAMA_MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return response["message"]["content"]