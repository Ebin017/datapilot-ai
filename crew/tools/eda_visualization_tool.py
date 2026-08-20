from pydantic import Field
from crewai.tools import BaseTool

from crew.context.project_context_manager import (
    ProjectContextManager,
)

from services.eda_visualization.eda_visualization_service import (
    EDAVisualizationService,
)


class EDAVisualizationTool(BaseTool):
    """
    Generates exploratory data analysis visualizations.
    """

    name: str = "EDA Visualization Tool"

    description: str = (
        "Generate exploratory data analysis visualizations "
        "from the cleaned dataset using the AnalysisPlan stored "
        "in the shared ProjectContext. The visualizations include "
        "histograms, boxplots, categorical count plots, correlation "
        "heatmaps, and target distribution charts. "
        "IMPORTANT: This tool takes NO arguments. "
        "Do not provide dataset, columns, target, project_context, "
        "analysis_plan, or any other arguments. "
        "The tool reads all required information directly from "
        "the shared ProjectContext."
    )

    visualization_service: EDAVisualizationService = Field(
        default_factory=EDAVisualizationService,
    )

    def _run(self) -> str:

        context = ProjectContextManager.get_context()

        if context.analysis_plan is None:
            raise ValueError(
                "Analysis plan is missing from ProjectContext. "
                "Run Analysis Planning before visualization."
            )

        context.eda_visualization_result = (
            self.visualization_service.generate(
                context,
            )
        )

        total = len(
            context.eda_visualization_result.chart_paths
        )

        return (
            "EDA visualizations generated successfully.\n"
            f"Charts Generated: {total}"
        )