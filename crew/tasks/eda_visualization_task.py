from crewai import Task

from crew.tools.eda_visualization_tool import (
    EDAVisualizationTool,
)


def create_eda_visualization_task(agent) -> Task:

    return Task(
        description=(
            "Generate exploratory data analysis visualizations "
            "for the cleaned dataset using the shared "
            "ProjectContext.\n\n"

            "The AnalysisPlan must already exist in "
            "ProjectContext.\n\n"

            "Use the EDA Visualization Tool to generate:\n"
            "- Histograms for numerical columns\n"
            "- Boxplots for numerical columns\n"
            "- Count plots for categorical columns\n"
            "- A correlation heatmap when enough numerical "
            "features are available\n"
            "- A target distribution chart\n\n"

            "Do not load the dataset again.\n"
            "Do not generate a new analysis plan.\n"
            "Do not provide arguments to the visualization tool.\n\n"

            "The tool should read the dataset and AnalysisPlan "
            "directly from ProjectContext and store the generated "
            "chart paths in EDAVisualizationResult."
        ),

        expected_output=(
            "A concise confirmation containing the total number "
            "of charts generated. Do not invent chart names or "
            "additional findings that are not returned by the tool."
        ),

        agent=agent,

        tools=[
            EDAVisualizationTool(),
        ],
    )