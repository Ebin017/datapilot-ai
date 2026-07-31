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
        "Generate histograms, boxplots, count plots, "
        "correlation heatmaps and target distribution charts."
    )

    visualization_service: EDAVisualizationService = Field(
        default_factory=EDAVisualizationService,
    )

    def _run(self) -> str:

        context = ProjectContextManager.get_context()

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