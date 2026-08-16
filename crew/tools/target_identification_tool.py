from pydantic import Field
from crewai.tools import BaseTool

from crew.context.project_context_manager import (
    ProjectContextManager,
)

from services.understanding.ai_target_identification_service import (
    AITargetIdentificationService,
)


class TargetIdentificationTool(BaseTool):
    """
    Identifies the most likely prediction target using AI.
    """

    name: str = "Target Identification Tool"

    description: str = (
        "Identify the most likely prediction target from the "
        "dataset stored in the shared ProjectContext. "
        "IMPORTANT: This tool takes NO arguments. "
        "Do not provide project_context, dataset, columns, "
        "target_column, or any other arguments. "
        "The tool reads all required information directly "
        "from the shared ProjectContext."
    )

    target_identification_service: (
        AITargetIdentificationService
    ) = Field(
        default_factory=AITargetIdentificationService,
    )

    def _run(self) -> str:

        context = ProjectContextManager.get_context()

        if context.dataset_info is None:
            raise ValueError(
                "Dataset metadata is missing from ProjectContext."
            )

        if context.data_quality is None:
            raise ValueError(
                "Data quality results are missing from ProjectContext."
            )

        if context.dataset_understanding is None:
            raise ValueError(
                "Dataset understanding is missing from ProjectContext. "
                "Run Dataset Understanding first."
            )

        context.target_suggestion = (
            self.target_identification_service.identify(
                context,
            )
        )

        target = context.target_suggestion

        if target is None:
            raise ValueError(
                "Target identification returned no result."
            )

        return (
            "Target identification completed successfully.\n"
            f"Target Column: {target.column_name}\n"
            f"Problem Type: {target.problem_type.value}\n"
            f"Confidence: {target.confidence:.2f}"
        )