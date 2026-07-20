from typing import Any

from pydantic import BaseModel, ConfigDict


class ModelTrainingResult(BaseModel):

    model_config = ConfigDict(
        arbitrary_types_allowed=True,
    )

    trained_models: dict[str, Any]

    evaluation_scores: dict[str, float]

    best_model_name: str

    best_score: float

    x_train: Any
    x_test: Any
    
    y_train: Any
    y_test: Any