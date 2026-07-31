from pydantic import Field
from crewai.tools import BaseTool

from crew.context.project_context_manager import (
    ProjectContextManager,
)
from services.understanding.dataset_understanding_service import (
    DatasetUnderstandingService,
)


class DatasetUnderstandingTool(BaseTool):
    """
    Uses AI to generate a high-level understanding of the dataset.
    """

    name: str = "Dataset Understanding Tool"

    description: str = (
        "Analyze the cleaned dataset and generate an AI-powered "
        "summary, likely problem type, and key observations."
    )

    dataset_understanding_service: DatasetUnderstandingService = Field(
        default_factory=DatasetUnderstandingService,
    )

    def _run(self) -> str:

        context = ProjectContextManager.get_context()

        context.dataset_understanding = (
            self.dataset_understanding_service.understand(
                context,
            )
        )

        understanding = context.dataset_understanding

        return (
            "Dataset understanding completed successfully.\n"
            f"Likely Problem Type: "
            f"{understanding.likely_problem_type.value}\n"
            f"Observations: {len(understanding.observations)}"
        )