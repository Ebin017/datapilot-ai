import pandas as pd

from models.dataset_info import DatasetInfo


class MetadataService:
    """
    Extracts metadata from a pandas DataFrame.
    """

    def extract(
        self,
        dataframe: pd.DataFrame,
        file_name: str,
    ) -> DatasetInfo:

        return DatasetInfo(
            file_name=file_name,
            rows=len(dataframe),
            columns=len(dataframe.columns),
            column_names=list(dataframe.columns),

            data_types={
                column: str(dtype)
                for column, dtype in dataframe.dtypes.items()
            },

            numeric_columns=list(
                dataframe.select_dtypes(include="number").columns
            ),

            categorical_columns=list(
                dataframe.select_dtypes(include="object").columns
            ),

            datetime_columns=list(
                dataframe.select_dtypes(include="datetime").columns
            ),

            missing_values=dataframe.isnull().sum().to_dict(),

            duplicate_rows=int(dataframe.duplicated().sum()),

            memory_usage_mb=round(
                dataframe.memory_usage(deep=True).sum() / (1024 ** 2),
                2,
            ),
        )