from datetime import datetime

from pydantic import BaseModel, Field


class DatasetInfo(BaseModel):
    """
    Stores metadata about an uploaded dataset.
    """

    file_name: str
    rows: int
    columns: int
    column_names: list[str]

    data_types: dict[str, str] | None = None
    numeric_columns: list[str] | None = None
    categorical_columns: list[str] | None = None
    datetime_columns: list[str] | None = None

    memory_usage_mb: float | None = None

    created_at: datetime = Field(default_factory=datetime.now)