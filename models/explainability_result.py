from pydantic import BaseModel


class ExplainabilityResult(BaseModel):
    """
    Stores SHAP explainability results.
    """

    feature_importance: dict[str, float]

    top_features: list[str]

    shap_values: list[list[float]]

    expected_value: float | list[float]