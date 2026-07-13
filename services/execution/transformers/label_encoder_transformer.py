import pandas as pd
from sklearn.preprocessing import LabelEncoder


class LabelEncoderTransformer:

    def __init__(self):
        self.encoder = LabelEncoder()

    def transform(
        self,
        target: pd.Series,
    ) -> pd.Series:

        encoded = self.encoder.fit_transform(target)

        return pd.Series(
            encoded,
            index=target.index,
            name=target.name,
        )