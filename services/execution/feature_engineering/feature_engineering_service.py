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

        plan = context.analysis_plan
        dataset_info = context.dataset_info

        # Drop excluded columns
        dataframe = dataframe.drop(
            columns=plan.columns_to_drop,
            errors="ignore",
        )

        target_column = plan.target_column

        # Separate target
        target = dataframe[target_column]

        # Separate features
        features = dataframe.drop(
            columns=[target_column],
        )

        # -----------------------------
        # Determine feature columns
        # -----------------------------

        categorical_features = [
            column
            for column in dataset_info.categorical_columns
            if column != target_column
            and column not in plan.columns_to_drop
        ]

        numerical_features = [
            column
            for column in dataset_info.numeric_columns
            if column != target_column
            and column not in plan.columns_to_drop
        ]

        # -----------------------------
        # Encode target
        # -----------------------------

        if plan.target_encoding == "label":
            target = self.label_encoder.transform(target)

        # -----------------------------
        # Encode categorical features
        # -----------------------------

        if (
            plan.feature_encoding == "one_hot"
            and categorical_features
        ):
            features = self.one_hot_encoder.transform(
                features,
                categorical_features,
            )

        # -----------------------------
        # Scale numerical features
        # -----------------------------

        if (
            plan.scaling_method == "standard"
            and numerical_features
        ):
            features = self.scaler.transform(
                features,
                numerical_features,
            )

        return FeatureEngineeringResult(
            features=features,
            target=target,
            feature_names=list(features.columns),
        )