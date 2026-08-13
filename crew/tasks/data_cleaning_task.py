from crewai import Task

from crew.tools.data_cleaning_tool import (
    DataCleaningTool,
)


def create_data_cleaning_task(agent) -> Task:

    return Task(
        description=(
            "Execute the cleaning strategy that has already "
            "been generated and stored in the shared "
            "ProjectContext.\n\n"

            "Use the Data Cleaning Tool to apply the strategy "
            "to the loaded dataset.\n\n"

            "Do not generate a new cleaning strategy. "
            "Do not load the dataset again."
        ),

        expected_output=(
            "The cleaning strategy has been successfully "
            "executed and the shared ProjectContext contains "
            "the cleaned dataset and data cleaning results."
        ),

        agent=agent,

        tools=[
            DataCleaningTool(),
        ],
    )