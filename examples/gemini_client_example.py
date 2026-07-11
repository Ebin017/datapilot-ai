from clients.llm.gemini_client import GeminiClient


def main():
    client = GeminiClient()

    response = client.generate(
        "Explain supervised machine learning in two sentences."
    )

    print(response)


if __name__ == "__main__":
    main()