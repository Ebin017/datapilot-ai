from pydantic import Field
from crewai.tools import BaseTool

from crew.context.project_context_manager import (
    ProjectContextManager,
)

from services.evaluation.model_evaluation_service import (
    ModelEvaluationService,
)


class ModelEvaluationTool(BaseTool):
    """
    Evaluates the best trained machine learning model.
    """

    name: str = "Model Evaluation Tool"

    description: str = (
        "Evaluate the best trained machine learning model "
        "using classification metrics."
    )

    evaluation_service: ModelEvaluationService = Field(
        default_factory=ModelEvaluationService,
    )

    def _run(self) -> str:

        context = ProjectContextManager.get_context()

        context.model_evaluation_result = (
            self.evaluation_service.evaluate(
                context,
            )
        )

        result = context.model_evaluation_result

        return (
            "Model evaluation completed successfully.\n"
            f"Accuracy: {result.accuracy:.4f}\n"
            f"Precision: {result.precision:.4f}\n"
            f"Recall: {result.recall:.4f}\n"
            f"F1 Score: {result.f1_score:.4f}"
        )