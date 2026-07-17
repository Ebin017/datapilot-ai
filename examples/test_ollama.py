from clients.llm.ollama_client import OllamaClient

client = OllamaClient()

prompt = """
You are an API.

Return ONLY valid JSON.

{
    "problem_type": "",
    "target": ""
}

Dataset:
Columns:
- Age (number)
- Income (number)
- Churn (Yes/No)
"""

print(client.generate(prompt))