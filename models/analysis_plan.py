from pydantic import BaseModel

from models.enums.problem_type import ProblemType


class AnalysisPlan(BaseModel):
    """
    Defines how the dataset should be analyzed.
    """

    target_column: str

    problem_type: ProblemType

    evaluation_metric: str

    train_test_split: float

    random_state: int

    stratify_split: bool

    preprocessing_steps: list[str]