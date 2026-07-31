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
        "Analyze the dataset and identify the most likely "
        "target column for machine learning."
    )

    target_identification_service: (
        AITargetIdentificationService
    ) = Field(
        default_factory=AITargetIdentificationService,
    )

    def _run(self) -> str:

        context = ProjectContextManager.get_context()

        context.target_suggestion = (
            self.target_identification_service.identify(
                context,
            )
        )

        target = context.target_suggestion

        return (
            "Target identification completed successfully.\n"
            f"Target Column: {target.column_name}\n"
            f"Problem Type: {target.problem_type.value}\n"
            f"Confidence: {target.confidence:.2f}"
        )