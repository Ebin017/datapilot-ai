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
        "Clean the loaded dataset using the generated cleaning plan."
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

        return (
            "Data cleaning completed successfully.\n"
            f"Original Rows: {result.original_rows}\n"
            f"Final Rows: {result.final_rows}\n"
            f"Duplicate Rows Removed: {result.duplicate_rows_removed}\n"
            f"Columns Removed: {len(result.columns_removed)}\n"
            f"Missing Value Columns Handled: "
            f"{len(result.missing_values_filled)}"
        )