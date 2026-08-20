from crewai import Task

from crew.tools.eda_tool import EDATool


def create_eda_task(agent) -> Task:

    return Task(
        description=(
            "Perform exploratory data analysis on the cleaned "
            "dataset using the existing shared ProjectContext.\n\n"

            "The AnalysisPlan must already exist in ProjectContext.\n\n"

            "Use the EDA Tool to calculate:\n"
            "- Numerical feature summaries\n"
            "- Categorical feature summaries\n"
            "- Correlation matrix for numerical features\n"
            "- Target distribution for classification problems\n\n"

            "Do not load the dataset again.\n"
            "Do not generate a new analysis plan.\n"
            "Do not provide arguments to the EDA Tool.\n\n"

            "Report the EDA Tool result exactly as returned. "
            "Do not add interpretations or invent additional "
            "findings that are not present in the tool output."
        ),

        expected_output=(
            "A concise EDA completion summary containing the "
            "number of numerical features, number of categorical "
            "features, whether the correlation matrix is available, "
            "and whether target distribution is available."
        ),

        agent=agent,

        tools=[
            EDATool(),
        ],
    )