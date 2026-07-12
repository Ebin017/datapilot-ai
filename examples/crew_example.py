from crew.ai_consulting_crew import AIConsultingCrew


def main():

    prompt = """
Return JSON:

{
    "summary":"Test",
    "likely_problem_type":"classification",
    "observations":[
        "one",
        "two",
        "three"
    ]
}
"""

    crew = AIConsultingCrew()

    result = crew.understand_dataset(
        prompt,
    )

    print(result)


if __name__ == "__main__":
    main()