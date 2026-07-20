from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
)

from context.project_context import ProjectContext
from models import ModelEvaluationResult


class ModelEvaluationService:
    """
    Evaluates the best trained model.
    """

    def evaluate(
        self,
        context: ProjectContext,
    ) -> ModelEvaluationResult:

        training = context.model_training_result

        model = training.trained_models[
            training.best_model_name
        ]

        predictions = model.predict(
            training.x_test,
        )

        return ModelEvaluationResult(
            accuracy=accuracy_score(
                training.y_test,
                predictions,
            ),
            precision=precision_score(
                training.y_test,
                predictions,
            ),
            recall=recall_score(
                training.y_test,
                predictions,
            ),
            f1_score=f1_score(
                training.y_test,
                predictions,
            ),
            confusion_matrix=confusion_matrix(
                training.y_test,
                predictions,
            ).tolist(),
            classification_report=classification_report(
                training.y_test,
                predictions,
                output_dict=True,
            ),
        )