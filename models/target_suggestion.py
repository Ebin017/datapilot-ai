from pydantic import BaseModel

from models.enums.problem_type import ProblemType


class TargetSuggestion(BaseModel):
    """
    Represents the recommended prediction target.
    """

    column_name: str

    problem_type: ProblemType

    confidence: float

    reason: str