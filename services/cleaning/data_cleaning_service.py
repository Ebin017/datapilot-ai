import pandas as pd

from context.project_context import ProjectContext
from models.cleaning_plan import (
    CleaningPlan,
    CleaningStrategy,
)
from models.data_cleaning_result import DataCleaningResult


class DataCleaningService:
    """
    Executes the cleaning plan and updates the dataframe.
    """

    def clean(
        self,
        context: ProjectContext,
        cleaning_plan: CleaningPlan,
    ) -> DataCleaningResult:

        df = context.dataframe.copy()

        original_rows = len(df)

        duplicate_rows_removed = 0
        missing_values_filled = {}
        columns_removed = []
        datatype_conversions = {}
        cleaning_summary = []

        # ------------------------------------------
        # Remove duplicate rows
        # ------------------------------------------

        if cleaning_plan.remove_duplicates:

            duplicate_rows_removed = df.duplicated().sum()

            if duplicate_rows_removed > 0:

                df = df.drop_duplicates()

                cleaning_summary.append(
                    f"Removed {duplicate_rows_removed} duplicate rows."
                )

        # ------------------------------------------
        # Drop unnecessary columns
        # ------------------------------------------

        for column in cleaning_plan.columns_to_drop:

            if column in df.columns:

                df = df.drop(columns=column)

                columns_removed.append(column)

                cleaning_summary.append(
                    f"Dropped column '{column}'."
                )

        # ------------------------------------------
        # Fill missing values
        # ------------------------------------------

        for (
            column,
            strategy,
        ) in cleaning_plan.column_strategies.items():

            if column not in df.columns:
                continue

            missing_count = df[column].isna().sum()

            if missing_count == 0:
                continue

            if strategy.strategy == CleaningStrategy.MEAN:

                value = df[column].mean()

                df[column] = df[column].fillna(value)

            elif strategy.strategy == CleaningStrategy.MEDIAN:

                value = df[column].median()

                df[column] = df[column].fillna(value)

            elif strategy.strategy == CleaningStrategy.MODE:

                mode = df[column].mode()

                if not mode.empty:

                    df[column] = df[column].fillna(mode.iloc[0])

            elif strategy.strategy == CleaningStrategy.DROP_ROWS:

                before = len(df)

                df = df.dropna(subset=[column])

                missing_count = before - len(df)

            elif strategy.strategy == CleaningStrategy.NONE:

                continue

            missing_values_filled[column] = missing_count

            cleaning_summary.append(
                f"{column}: handled {missing_count} missing values using "
                f"{strategy.strategy.value}."
            )

        # ------------------------------------------
        # Trim whitespace
        # ------------------------------------------

        if cleaning_plan.trim_whitespace:

            object_columns = df.select_dtypes(
                include=["object"]
            ).columns

            for column in object_columns:

                df[column] = (
                    df[column]
                    .astype(str)
                    .str.strip()
                    .replace("nan", pd.NA)
                )

            cleaning_summary.append(
                "Trimmed whitespace from string columns."
            )

        # ------------------------------------------
        # Update Project Context
        # ------------------------------------------

        context.dataframe = df

        return DataCleaningResult(
            original_rows=original_rows,
            final_rows=len(df),
            duplicate_rows_removed=duplicate_rows_removed,
            missing_values_filled=missing_values_filled,
            columns_removed=columns_removed,
            datatype_conversions=datatype_conversions,
            cleaning_summary=cleaning_summary,
        )