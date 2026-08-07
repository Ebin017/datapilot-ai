from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)

from models import ModelEvaluationResult


class RegressionEvaluator:
    """
    Evaluates regression models.
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

        mse = mean_squared_error(
            y_test,
            predictions,
        )

        rmse = mse ** 0.5

        return ModelEvaluationResult(
            metrics={
                "mae": mean_absolute_error(
                    y_test,
                    predictions,
                ),
                "mse": mse,
                "rmse": rmse,
                "r2": r2_score(
                    y_test,
                    predictions,
                ),
            },
        )