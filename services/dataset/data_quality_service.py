import pandas as pd

from models.data_quality_result import DataQualityResult


class DataQualityService:
    """
    Evaluates the quality of a dataset.
    """

    def analyze(
        self,
        dataframe: pd.DataFrame,
    ) -> DataQualityResult:

        total_rows = len(dataframe)

        missing_values = dataframe.isnull().sum().to_dict()

        missing_percentages = {
            column: (
                round((count / total_rows) * 100, 2)
                if total_rows > 0
                else 0.0
            )
            for column, count in missing_values.items()
        }

        duplicate_rows = int(dataframe.duplicated().sum())

        duplicate_percentage = (
            round((duplicate_rows / total_rows) * 100, 2)
            if total_rows > 0
            else 0.0
        )

        constant_columns = [
            column
            for column in dataframe.columns
            if dataframe[column].nunique(dropna=False) == 1
        ]

        empty_columns = [
            column
            for column in dataframe.columns
            if dataframe[column].isnull().all()
        ]

        return DataQualityResult(
            missing_values=missing_values,
            missing_percentages=missing_percentages,
            duplicate_rows=duplicate_rows,
            duplicate_percentage=duplicate_percentage,
            constant_columns=constant_columns,
            empty_columns=empty_columns,
        )
