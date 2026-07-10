from enum import Enum


class ProblemType(str, Enum):
    """
    Supported machine learning problem types.
    """

    CLASSIFICATION = "classification"
    REGRESSION = "regression"