from pydantic import BaseModel


class EDAResult(BaseModel):
    """
    Stores the results of exploratory data analysis.
    """

    numerical_summary: dict[str, dict]

    categorical_summary: dict[str, dict]

    correlation_matrix: dict[str, dict]

    target_distribution: dict[str, int] | None = None