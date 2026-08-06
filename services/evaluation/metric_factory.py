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


class MetricFactory:
    """
    Creates evaluation metric functions.
    """

    @staticmethod
    def create(
        metric_name: str,
    ):

        metrics = {
            "accuracy": accuracy_score,
            "f1_score": f1_score,
            "precision": precision_score,
            "recall": recall_score,
            "roc_auc": roc_auc_score,
            "mse": mean_squared_error,
            "mae": mean_absolute_error,
            "r2": r2_score,
        }

        if metric_name not in metrics:
            raise ValueError(
                f"Unsupported evaluation metric: {metric_name}"
            )

        return metrics[metric_name]