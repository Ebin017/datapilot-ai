from pydantic import Field
from crewai.tools import BaseTool

from crew.context.project_context_manager import (
    ProjectContextManager,
)
from services.cleaning.data_cleaning_service import (
    DataCleaningService,
)


class DataCleaningTool(BaseTool):
    """
    Executes the generated cleaning plan and updates the dataset.
    """

    name: str = "Data Cleaning Tool"

    description: str = (
        "Execute the cleaning plan already stored in the shared "
        "ProjectContext. "
        "IMPORTANT: This tool takes NO arguments. "
        "Do not provide strategy, columns_to_fillna, operations, "
        "or any other parameters. "
        "The tool automatically reads the cleaning plan from "
        "the shared ProjectContext."
    )

    data_cleaning_service: DataCleaningService = Field(
        default_factory=DataCleaningService,
    )

    def _run(self) -> str:

        context = ProjectContextManager.get_context()

        context.data_cleaning_result = (
            self.data_cleaning_service.clean(
                context=context,
                cleaning_plan=context.cleaning_plan,
            )
        )

        result = context.data_cleaning_result

        missing_value_details = (
            "\n".join(
                f"- {column}: {count} missing values"
                for column, count
                in result.missing_values_filled.items()
            )
            if result.missing_values_filled
            else "- None"
        )

        columns_removed = (
            ", ".join(result.columns_removed)
            if result.columns_removed
            else "None"
        )

        cleaning_summary = (
            "\n".join(
                f"- {summary}"
                for summary in result.cleaning_summary
            )
            if result.cleaning_summary
            else "- No cleaning operations performed."
        )

        return (
            "Data cleaning completed successfully.\n\n"

            f"Original Rows: {result.original_rows}\n"
            f"Final Rows: {result.final_rows}\n"
            f"Duplicate Rows Removed: "
            f"{result.duplicate_rows_removed}\n"
            f"Columns Removed: {columns_removed}\n\n"

            "Missing Value Details:\n"
            f"{missing_value_details}\n\n"

            "Cleaning Summary:\n"
            f"{cleaning_summary}"
        )