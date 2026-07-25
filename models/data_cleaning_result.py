from pydantic import BaseModel


class DataCleaningResult(BaseModel):
    """
    Stores the results of data cleaning.
    """

    original_rows: int

    final_rows: int

    duplicate_rows_removed: int

    missing_values_filled: dict[str, int]

    columns_removed: list[str]

    datatype_conversions: dict[str, str]

    cleaning_summary: list[str]