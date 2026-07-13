import pandas as pd
from sklearn.preprocessing import OneHotEncoder


class OneHotEncoderTransformer:
    """
    Encodes categorical feature columns using one-hot encoding.
    """

    def __init__(self):
        self.encoder = OneHotEncoder(
            sparse_output=False,
            handle_unknown="ignore",
        )

    def transform(
        self,
        features: pd.DataFrame,
        categorical_columns: list[str],
    ) -> pd.DataFrame:

        transformed = features.copy()

        if not categorical_columns:
            return transformed

        encoded = self.encoder.fit_transform(
            transformed[categorical_columns]
        )

        encoded_columns = self.encoder.get_feature_names_out(
            categorical_columns
        )

        encoded_dataframe = pd.DataFrame(
            encoded,
            columns=encoded_columns,
            index=transformed.index,
        )

        transformed = transformed.drop(
            columns=categorical_columns
        )

        transformed = pd.concat(
            [
                transformed,
                encoded_dataframe,
            ],
            axis=1,
        )

        return transformed