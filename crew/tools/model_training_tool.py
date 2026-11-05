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
        "Train candidate machine learning models using the "
        "AnalysisPlan and FeatureEngineeringResult stored in the "
        "shared ProjectContext, evaluate their performance, and "
        "select the best-performing model. "
        "IMPORTANT: This tool takes NO arguments. "
        "Do not provide dataset, features, target, analysis_plan, "
        "project_context, model names, or any other arguments. "
        "The tool reads all required information directly from "
        "the shared ProjectContext."
    )

    training_service: ModelTrainingService = Field(
        default_factory=ModelTrainingService,
    )

    def _run(self) -> str:

        context = ProjectContextManager.get_context()

        if context.analysis_plan is None:
            raise ValueError(
                "Analysis plan is missing from ProjectContext. "
                "Run Analysis Planning before Model Training."
            )

        if context.feature_engineering_result is None:
            raise ValueError(
                "Feature engineering result is missing from "
                "ProjectContext. Run Feature Engineering before "
                "Model Training."
            )

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