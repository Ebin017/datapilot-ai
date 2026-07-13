import pandas as pd

from context.project_context import ProjectContext
from models import FeatureEngineeringResult

from services.execution.transformers.label_encoder_transformer import (
    LabelEncoderTransformer,
)

from services.execution.transformers.one_hot_encoder_transformer import (
    OneHotEncoderTransformer,
)

from services.execution.transformers.standard_scaler_transformer import (
    StandardScalerTransformer,
)


class FeatureEngineeringService:
    """
    Performs feature engineering based on the analysis plan.
    """

    def __init__(self):
        self.label_encoder = LabelEncoderTransformer()
        self.one_hot_encoder = OneHotEncoderTransformer()
        self.scaler = StandardScalerTransformer()

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

        target_column = context.analysis_plan.target_column

        # Separate target
        target = dataframe[target_column]

        # Separate features
        features = dataframe.drop(
            columns=[target_column],
        )

        # Encode target
        if context.analysis_plan.target_encoding == "label":
            target = self.label_encoder.transform(target)

        # Encode categorical features
        if context.analysis_plan.feature_encoding == "one_hot":
            features = self.one_hot_encoder.transform(
                features,
                context.analysis_plan.categorical_features,
            )

        # Scale numerical features
        if context.analysis_plan.scaling_method == "standard":
            features = self.scaler.transform(
                features,
                context.analysis_plan.numerical_features,
            )

        return FeatureEngineeringResult(
            features=features,
            target=target,
            feature_names=list(features.columns),
        )