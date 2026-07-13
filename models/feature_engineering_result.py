import pandas as pd
from pydantic import BaseModel, ConfigDict


class FeatureEngineeringResult(BaseModel):
    """
    Stores the processed dataset ready for model training.
    """

    model_config = ConfigDict(arbitrary_types_allowed=True)

    features: pd.DataFrame

    target: pd.Series

    feature_names: list[str]