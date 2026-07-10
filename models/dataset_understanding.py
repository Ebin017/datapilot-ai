from pydantic import BaseModel

from models.enums.problem_type import ProblemType


class DatasetUnderstanding(BaseModel):
    """
    Represents the AI's understanding of a dataset.
    """

    summary: str

    likely_problem_type: ProblemType

    observations: list[str]