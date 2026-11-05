from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.linear_model import LogisticRegression, LinearRegression


class ModelFactory:
    """
    Creates machine learning models.
    """

    @staticmethod
    def create(model_name: str):

        model_name = (
            model_name.strip()
            .lower()
            .replace(" ", "")
            .replace("_", "")
        )

        models = {
            "logisticregression": LogisticRegression(
                max_iter=1000,
            ),
            "randomforest": RandomForestClassifier(
                random_state=42,
            ),
            "linearregression": LinearRegression(),
            "randomforestregressor": RandomForestRegressor(
                random_state=42,
            ),
            "randomforestregression": RandomForestRegressor(
                random_state=42,
            ),
        }

        if model_name not in models:
            raise ValueError(
                f"Unsupported model: {model_name}"
            )

        return models[model_name]