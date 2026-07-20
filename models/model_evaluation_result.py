from pydantic import BaseModel


class ModelEvaluationResult(BaseModel):
    """
    Stores model evaluation metrics.
    """

    accuracy: float

    precision: float

    recall: float

    f1_score: float

    confusion_matrix: list[list[int]]

    classification_report: dict