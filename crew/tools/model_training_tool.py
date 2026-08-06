from pydantic import Field
from crewai.tools import BaseTool

from crew.context.project_context_manager import (
    ProjectContextManager,
)

from services.training.model_training_service import (
    ModelTrainingService,
)


class ModelTrainingTool(BaseTool):
    """
    Trains machine learning models based on the analysis plan.
    """

    name: str = "Model Training Tool"

    description: str = (
        "Train candidate machine learning models and select "
        "the best performing model."
    )

    training_service: ModelTrainingService = Field(
        default_factory=ModelTrainingService,
    )

    def _run(self) -> str:

        context = ProjectContextManager.get_context()

        context.model_training_result = (
            self.training_service.train(
                context,
            )
        )

        result = context.model_training_result

        return (
            "Model training completed successfully.\n"
            f"Models Trained: {len(result.trained_models)}\n"
            f"Best Model: {result.best_model_name}\n"
            f"Best Score: {result.best_score:.4f}"
        )