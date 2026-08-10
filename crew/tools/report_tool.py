from pydantic import Field
from crewai.tools import BaseTool

from crew.context.project_context_manager import (
    ProjectContextManager,
)

from services.reporting.report_service import (
    ReportService,
)


class ReportTool(BaseTool):
    """
    Generates the final DataPilot AI PDF report.
    """

    name: str = "Report Generation Tool"

    description: str = (
        "Generate a comprehensive PDF report containing "
        "dataset analysis, data quality, cleaning, EDA, "
        "machine learning results, explainability, and "
        "business insights."
    )

    report_service: ReportService = Field(
        default_factory=ReportService,
    )

    def _run(self) -> str:

        context = ProjectContextManager.get_context()

        result = self.report_service.generate(
            context,
        )

        context.report_result = result

        return (
            "Report generated successfully.\n"
            f"Report Path: {result.report_path}"
        )