import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    """
    Application configuration loaded from environment variables.
    """

    # Gemini
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

    GEMINI_MODEL = os.getenv(
        "GEMINI_MODEL",
        "gemini-2.5-flash",
    )

    # Ollama
    LLM_PROVIDER = os.getenv(
        "LLM_PROVIDER",
        "gemini",
    )

    OLLAMA_MODEL = os.getenv(
        "OLLAMA_MODEL",
        "llama3.2:1b",
    )