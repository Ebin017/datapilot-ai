from crewai import Task

from crew.tools.cleaning_strategy_tool import (
    CleaningStrategyTool,
)


def create_cleaning_strategy_task(agent) -> Task:

    return Task(
        description=(
            "Generate a cleaning strategy for the dataset "
            "using the existing ProjectContext.\n\n"

            "Use the available dataset metadata and data "
            "quality results to determine the appropriate "
            "cleaning operations.\n\n"

            "Do not clean the dataset in this task. "
            "Only generate and store the cleaning strategy "
            "in the shared ProjectContext."
        ),

        expected_output=(
            "A completed cleaning strategy stored in the "
            "shared ProjectContext, including missing-value "
            "strategies, columns to drop, duplicate handling, "
            "and whitespace handling."
        ),

        agent=agent,

        tools=[
            CleaningStrategyTool(),
        ],
    )