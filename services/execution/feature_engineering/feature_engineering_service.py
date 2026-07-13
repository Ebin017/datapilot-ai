import pandas as pd

from context.project_context import ProjectContext
from models import FeatureEngineeringResult

from services.execution.transformers.label_encoder_transformer import (
    LabelEncoderTransformer,
)


class FeatureEngineeringService:
    """
    Performs feature engineering based on the analysis plan.
    """

    def __init__(self):
        self.label_encoder = LabelEncoderTransformer()

    def transform(
        self,
        context: ProjectContext,
    ) -> FeatureEngineeringResult:

        dataframe = context.dataframe.copy()

        # Drop excluded columns
        dataframe = dataframe.drop(
            columns=context.analysis_plan.columns_to_drop,
            errors="ignore",
        )

        # Separate features and target
        target_column = context.analysis_plan.target_column

        target = dataframe[target_column]

        if context.analysis_plan.target_encoding == "label":
            target = self.label_encoder.transform(target)

        features = dataframe.drop(
            columns=[target_column],
        )

        return FeatureEngineeringResult(
            features=features,
            target=target,
            feature_names=list(features.columns),
        )