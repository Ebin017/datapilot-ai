from google import genai

from config.settings import Settings


class GeminiClient:
    """
    Client for communicating with Google's Gemini models.
    """

    def __init__(self):
        self.client = genai.Client(
            api_key=Settings.GEMINI_API_KEY,
        )

    def generate(
        self,
        prompt: str,
    ) -> str:

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        return response.text