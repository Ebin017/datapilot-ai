from pydantic import BaseModel


class EDAVisualizationResult(BaseModel):
    """
    Stores the paths of all generated EDA charts.
    """

    chart_paths: list[str]