from crewai import Task

from crew.tools.analysis_planning_tool import (
    AnalysisPlanningTool,
)


def create_analysis_planning_task(agent) -> Task:

    return Task(
        description=(
            "Create the machine learning analysis plan using "
            "the information already stored in the shared "
            "ProjectContext.\n\n"

            "The dataset understanding and target "
            "identification tasks have already been completed.\n\n"

            "Use the Analysis Planning Tool exactly once.\n\n"

            "The tool requires NO arguments. Do not pass "
            "target_column, problem_type, candidate_models, "
            "or any other arguments to the tool.\n\n"

            "The tool reads all required information directly "
            "from the shared ProjectContext and stores the "
            "generated AnalysisPlan there.\n\n"

            "After the Analysis Planning Tool executes "
            "successfully, do not call it again. Do not "
            "manually create or modify an analysis plan."
        ),

        expected_output=(
            "Confirmation that the Analysis Planning Tool "
            "successfully generated and stored the AnalysisPlan "
            "in the shared ProjectContext."
        ),

        agent=agent,

        tools=[
            AnalysisPlanningTool(),
        ],
    )