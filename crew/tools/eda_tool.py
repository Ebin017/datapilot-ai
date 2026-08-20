from pydantic import Field
from crewai.tools import BaseTool

from crew.context.project_context_manager import (
    ProjectContextManager,
)

from services.execution.eda.exploratory_data_analysis_service import (
    ExploratoryDataAnalysisService,
)


class EDATool(BaseTool):
    """
    Performs exploratory data analysis on the cleaned dataset.
    """

    name: str = "EDA Tool"

    description: str = (
        "Perform exploratory data analysis on the cleaned dataset "
        "using the AnalysisPlan stored in the shared ProjectContext. "
        "The analysis includes numerical statistics, categorical "
        "summaries, correlations, and target distribution. "
        "IMPORTANT: This tool takes NO arguments. "
        "Do not provide dataset, columns, target, project_context, "
        "analysis_plan, or any other arguments. "
        "The tool reads all required information directly from "
        "the shared ProjectContext."
    )

    eda_service: ExploratoryDataAnalysisService = Field(
        default_factory=ExploratoryDataAnalysisService,
    )

    def _run(self) -> str:

        context = ProjectContextManager.get_context()

        if context.analysis_plan is None:
            raise ValueError(
                "Analysis plan is missing from ProjectContext. "
                "Run Analysis Planning first."
            )

        context.eda_result = (
            self.eda_service.analyze(
                context,
            )
        )

        result = context.eda_result

        return (
            "EDA completed successfully.\n"
            f"Numerical Features: "
            f"{len(result.numerical_summary)}\n"
            f"Categorical Features: "
            f"{len(result.categorical_summary)}\n"
            f"Correlation Matrix: "
            f"{'Available' if result.correlation_matrix else 'Not Available'}\n"
            f"Target Distribution: "
            f"{'Available' if result.target_distribution is not None else 'Not Available'}"
        )