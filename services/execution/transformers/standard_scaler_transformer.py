import pandas as pd
from sklearn.preprocessing import StandardScaler


class StandardScalerTransformer:
    """
    Scales numerical features using StandardScaler.
    """

    def __init__(self):
        self.scaler = StandardScaler()

    def transform(
        self,
        features: pd.DataFrame,
        numerical_columns: list[str],
    ) -> pd.DataFrame:

        transformed = features.copy()

        if not numerical_columns:
            return transformed

        transformed[numerical_columns] = self.scaler.fit_transform(
            transformed[numerical_columns]
        )

        return transformed