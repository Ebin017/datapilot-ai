from pydantic import BaseModel


class CandidateModel(BaseModel):
    """
    Represents a candidate machine learning model.
    """

    name: str

    reason: str