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

        metrics_text = "\n".join(
            f"{metric}: {value:.4f}"
            for metric, value in result.metrics.items()
        )

        return (
            "Model evaluation completed successfully.\n"
            f"{metrics_text}"
        )