from crewai import Task

from crew.tools.target_identification_tool import (
    TargetIdentificationTool,
)


def create_target_identification_task(agent) -> Task:

    return Task(
        description=(
            "Identify the most likely prediction target for "
            "the cleaned dataset stored in the shared "
            "ProjectContext.\n\n"

            "Use the Target Identification Tool to determine "
            "the target column, machine learning problem type, "
            "confidence, and reasoning.\n\n"

            "The dataset understanding result from the previous "
            "task is already available in ProjectContext.\n\n"

            "Do not load the dataset again and do not provide "
            "arguments to the tool."
        ),

        expected_output=(
            "A completed target suggestion stored in the "
            "shared ProjectContext containing the target "
            "column, problem type, confidence, and reason."
        ),

        agent=agent,

        tools=[
            TargetIdentificationTool(),
        ],
    )