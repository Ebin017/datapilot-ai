from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
)

from models import ModelEvaluationResult


class ClassificationEvaluator:
    """
    Evaluates classification models.
    """

    def evaluate(
        self,
        model,
        x_test,
        y_test,
    ) -> ModelEvaluationResult:

        predictions = model.predict(
            x_test,
        )

        return ModelEvaluationResult(
            metrics={
                "accuracy": accuracy_score(
                    y_test,
                    predictions,
                ),
                "precision": precision_score(
                    y_test,
                    predictions,
                ),
                "recall": recall_score(
                    y_test,
                    predictions,
                ),
                "f1_score": f1_score(
                    y_test,
                    predictions,
                ),
            },
            confusion_matrix=confusion_matrix(
                y_test,
                predictions,
            ).tolist(),
            classification_report=classification_report(
                y_test,
                predictions,
                output_dict=True,
            ),
        )