from pydantic import BaseModel


class DataQualityResult(BaseModel):
    """
    Stores the quality assessment of a dataset.
    """

    missing_values: dict[str, int]

    missing_percentages: dict[str, float]

    duplicate_rows: int

    duplicate_percentage: float

    constant_columns: list[str]

    empty_columns: list[str]
