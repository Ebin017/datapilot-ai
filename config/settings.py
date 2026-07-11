from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    """
    Application settings loaded from environment variables.
    """

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")