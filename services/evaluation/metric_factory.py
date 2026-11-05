import numpy as np

from sklearn.metrics import (
    accuracy_score,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
    mean_squared_error,
    mean_absolute_error,
    r2_score,
)


def root_mean_squared_error(y_true, y_pred):
    """
    Calculate Root Mean Squared Error.
    """
    return float(np.sqrt(mean_squared_error(y_true, y_pred)))


class MetricFactory:
    """
    Creates evaluation metric functions and determines
    whether higher or lower metric values are better.
    """

    METRICS = {
        "accuracy": accuracy_score,
        "f1_score": f1_score,
        "precision": precision_score,
        "recall": recall_score,
        "roc_auc": roc_auc_score,
        "mse": mean_squared_error,
        "mae": mean_absolute_error,
        "rmse": root_mean_squared_error,
        "r2": r2_score,
    }

    HIGHER_IS_BETTER = {
        "accuracy",
        "f1_score",
        "precision",
        "recall",
        "roc_auc",
        "r2",
    }

    @staticmethod
    def create(metric_name: str):
        metric_name = metric_name.lower()

        if metric_name not in MetricFactory.METRICS:
            raise ValueError(
                f"Unsupported evaluation metric: {metric_name}"
            )

        return MetricFactory.METRICS[metric_name]

    @staticmethod
    def is_higher_better(metric_name: str) -> bool:
        metric_name = metric_name.lower()

        if metric_name not in MetricFactory.METRICS:
            raise ValueError(
                f"Unsupported evaluation metric: {metric_name}"
            )

        return metric_name in MetricFactory.HIGHER_IS_BETTER