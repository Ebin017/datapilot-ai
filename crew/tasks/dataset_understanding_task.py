from crewai import Task


def create_dataset_understanding_task(
    agent,
    prompt: str,
) -> Task:
    """
    Creates the dataset understanding task.
    """

    return Task(
        description=prompt,

        expected_output=(
            "Valid JSON matching the DatasetUnderstanding schema."
        ),

        agent=agent,
    )