from context.project_context import ProjectContext
from models import ModelEvaluationResult

from services.evaluation.evaluation_factory import (
    EvaluationFactory,
)


class ModelEvaluationService:
    """
    Evaluates the best trained machine learning model.
    """

    def evaluate(
        self,
        context: ProjectContext,
    ) -> ModelEvaluationResult:

        training = context.model_training_result

        evaluator = EvaluationFactory.create(
            context.analysis_plan.problem_type,
        )

        return evaluator.evaluate(
            model=training.best_model,
            x_test=training.x_test,
            y_test=training.y_test,
        )