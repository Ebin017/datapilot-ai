from pydantic import BaseModel


class ModelEvaluationResult(BaseModel):
    """
    Stores model evaluation metrics.
    """

    metrics: dict[str, float]

    confusion_matrix: list[list[int]] | None = None

    classification_report: dict | None = None