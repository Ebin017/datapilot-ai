from pydantic import BaseModel

from models.enums.problem_type import ProblemType
from models import CandidateModel


class AnalysisPlan(BaseModel):
    """
    Stores the execution plan for a machine learning workflow.
    """

    target_column: str

    problem_type: ProblemType

    evaluation_metric: str

    train_test_split: float

    random_state: int

    stratify_split: bool

    columns_to_drop: list[str]

    numerical_features: list[str]

    categorical_features: list[str]

    scaling_method: str | None = None

    feature_encoding: str | None

    target_encoding: str | None

    candidate_models: list[CandidateModel]