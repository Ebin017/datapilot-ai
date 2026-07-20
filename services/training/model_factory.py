from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression


class ModelFactory:
    """
    Creates machine learning models.
    """

    @staticmethod
    def create(
        model_name: str,
    ):

        if model_name == "logistic_regression":
            return LogisticRegression(
                max_iter=1000,
            )

        if model_name == "random_forest":
            return RandomForestClassifier(
                random_state=42,
            )

        raise ValueError(
            f"Unsupported model: {model_name}"
        )