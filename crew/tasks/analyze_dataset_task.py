from crewai import Task

from crew.tools.data_analysis_tool import DataAnalysisTool


def create_analysis_task(agent):
    return Task(
        description=(
            "Analyze the given dataset and prepare it for "
            "machine learning."
        ),
        expected_output="A populated ProjectContext.",
        agent=agent,
        tools=[DataAnalysisTool()],
    )