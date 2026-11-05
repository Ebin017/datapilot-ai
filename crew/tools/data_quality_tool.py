from crewai.tools import BaseTool
from pydantic import Field

from crew.context.project_context_manager import (
    ProjectContextManager,
)
from services.dataset.data_quality_service import (
    DataQualityService,
)


class DataQualityTool(BaseTool):
    """
    Analyzes the quality of the loaded dataset and stores the
    result in ProjectContext.
    """

    name: str = "Data Quality Analyzer"

    description: str = (
        "Analyze missing values, duplicate rows, constant columns "
        "and empty columns in the dataset already loaded into "
        "ProjectContext. This tool uses the shared ProjectContext "
        "and does not need a filename. If a filename is accidentally "
        "provided, ignore it."
    )

    data_quality_service: DataQualityService = Field(
        default_factory=DataQualityService,
    )

    def _run(self, file_name: str | None = None) -> str:

        context = ProjectContextManager.get_context()

        if context is None:
            return (
                "Error: ProjectContext is not initialized. "
                "Load the dataset before running data quality analysis."
            )

        context.data_quality = (
            self.data_quality_service.analyze(
                context.dataframe,
            )
        )

        result = context.data_quality

        return (
            "Data quality analysis completed successfully.\n"
            f"Duplicate Rows: {result.duplicate_rows}\n"
            f"Duplicate Percentage: {result.duplicate_percentage}%\n"
            f"Constant Columns: {len(result.constant_columns)}\n"
            f"Empty Columns: {len(result.empty_columns)}"
        )