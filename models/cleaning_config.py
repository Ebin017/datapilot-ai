from pydantic import BaseModel


class CleaningConfig(BaseModel):
    """
    Configuration for data cleaning.
    """

    skewness_threshold: float = 1.0

    drop_column_missing_threshold: float = 0.50

    remove_duplicates: bool = True

    trim_whitespace: bool = True