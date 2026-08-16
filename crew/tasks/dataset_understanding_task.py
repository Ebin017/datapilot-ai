from crewai import Task

from crew.tools.dataset_understanding_tool import (
    DatasetUnderstandingTool,
)


def create_dataset_understanding_task(agent) -> Task:

    return Task(
        description=(
            "Analyze the cleaned dataset currently stored in "
            "the shared ProjectContext.\n\n"

            "Use the Dataset Understanding Tool to determine "
            "the likely machine learning problem type and "
            "generate high-level observations about the "
            "dataset.\n\n"

            "Do not load the dataset again and do not provide "
            "any arguments to the tool."
        ),

        expected_output=(
            "A completed dataset understanding result stored "
            "in the shared ProjectContext, including the likely "
            "problem type and key observations."
        ),

        agent=agent,

        tools=[
            DatasetUnderstandingTool(),
        ],
    )