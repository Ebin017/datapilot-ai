from enum import Enum

from pydantic import BaseModel


class CleaningStrategy(str, Enum):
    MEAN = "mean"
    MEDIAN = "median"
    MODE = "mode"
    DROP_COLUMN = "drop_column"
    DROP_ROWS = "drop_rows"
    NONE = "none"


class ColumnCleaningStrategy(BaseModel):
    strategy: CleaningStrategy

    reason: str

    missing_percentage: float

    skewness: float | None = None

    drop_column: bool = False


class CleaningPlan(BaseModel):

    column_strategies: dict[str, ColumnCleaningStrategy]

    columns_to_drop: list[str]

    remove_duplicates: bool

    trim_whitespace: bool

    datatype_conversions: dict[str, str]

    notes: list[str]