from pydantic import Field
from crewai.tools import BaseTool

from crew.context.project_context_manager import (
    ProjectContextManager,
)
from services.cleaning.cleaning_strategy_service import (
    CleaningStrategyService,
)


class CleaningStrategyTool(BaseTool):
    """
    Generates a cleaning strategy for the loaded dataset.
    """

    name: str = "Cleaning Strategy Generator"

    description: str = (
        "Generate the cleaning strategy for the dataset already "
        "stored in the shared ProjectContext. "
        "IMPORTANT: This tool takes NO arguments. "
        "Do not provide dataset_columns, rows, missing values, "
        "or any other parameters. "
        "The tool automatically reads the shared ProjectContext."
    )

    cleaning_strategy_service: CleaningStrategyService = Field(
        default_factory=CleaningStrategyService,
    )

    def _run(self) -> str:

        context = ProjectContextManager.get_context()

        context.cleaning_plan = (
            self.cleaning_strategy_service.generate_plan(
                context,
            )
        )

        plan = context.cleaning_plan

        return (
            "Cleaning strategy generated successfully.\n"
            f"Columns with strategies: {len(plan.column_strategies)}\n"
            f"Columns to drop: {len(plan.columns_to_drop)}\n"
            f"Remove duplicates: {plan.remove_duplicates}\n"
            f"Trim whitespace: {plan.trim_whitespace}"
        )