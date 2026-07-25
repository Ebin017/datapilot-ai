from pandas.api.types import (
    is_bool_dtype,
    is_string_dtype,
    is_datetime64_any_dtype,
    is_numeric_dtype,
    is_object_dtype,
)

from context.project_context import ProjectContext
from models.cleaning_config import CleaningConfig
from models.cleaning_plan import (
    CleaningPlan,
    CleaningStrategy,
    ColumnCleaningStrategy,
)


class CleaningStrategyService:
    """
    Generates a cleaning plan based on dataset statistics.
    """

    def __init__(self, config: CleaningConfig | None = None):
        self.config = config or CleaningConfig()

    def generate_plan(
        self,
        context: ProjectContext,
    ) -> CleaningPlan:
        """
        Analyze the dataset and generate a cleaning plan.
        """

        df = context.dataframe

        column_strategies = {}
        columns_to_drop = []
        datatype_conversions = {}
        notes = []

        for column in df.columns:

            series = df[column]

            missing_count = series.isna().sum()
            missing_percentage = series.isna().mean() * 100

            # --------------------------------------------------
            # Constant column
            # --------------------------------------------------

            if series.nunique(dropna=False) <= 1:

                columns_to_drop.append(column)

                notes.append(
                    f"{column}: Constant column detected."
                )

                column_strategies[column] = (
                    ColumnCleaningStrategy(
                        strategy=CleaningStrategy.DROP_COLUMN,
                        reason="Constant column.",
                        missing_percentage=missing_percentage,
                        drop_column=True,
                    )
                )

                continue

            # --------------------------------------------------
            # Too many missing values
            # --------------------------------------------------

            if (
                missing_percentage
                >= self.config.drop_column_missing_threshold * 100
            ):

                columns_to_drop.append(column)

                notes.append(
                    f"{column}: "
                    f"{missing_percentage:.1f}% missing values."
                )

                column_strategies[column] = (
                    ColumnCleaningStrategy(
                        strategy=CleaningStrategy.DROP_COLUMN,
                        reason="Too many missing values.",
                        missing_percentage=missing_percentage,
                        drop_column=True,
                    )
                )

                continue

            # --------------------------------------------------
            # No missing values
            # --------------------------------------------------

            if missing_count == 0:
                continue

            # --------------------------------------------------
            # Boolean column
            # --------------------------------------------------

            if is_bool_dtype(series):

                column_strategies[column] = (
                    ColumnCleaningStrategy(
                        strategy=CleaningStrategy.MODE,
                        reason="Boolean feature.",
                        missing_percentage=missing_percentage,
                    )
                )

                continue

            # --------------------------------------------------
            # Numeric column
            # --------------------------------------------------

            if is_numeric_dtype(series):

                skewness = series.dropna().skew()

                if abs(skewness) < self.config.skewness_threshold:

                    strategy = CleaningStrategy.MEAN
                    reason = (
                        "Approximately symmetric distribution."
                    )

                else:

                    strategy = CleaningStrategy.MEDIAN
                    reason = (
                        "Highly skewed distribution."
                    )

                column_strategies[column] = (
                    ColumnCleaningStrategy(
                        strategy=strategy,
                        reason=reason,
                        missing_percentage=missing_percentage,
                        skewness=round(skewness, 3),
                    )
                )

                continue

            # --------------------------------------------------
            # Datetime column
            # --------------------------------------------------

            if is_datetime64_any_dtype(series):

                column_strategies[column] = (
                    ColumnCleaningStrategy(
                        strategy=CleaningStrategy.NONE,
                        reason=(
                            "Datetime column. "
                            "Manual strategy recommended."
                        ),
                        missing_percentage=missing_percentage,
                    )
                )

                continue

            # --------------------------------------------------
            # Object / Categorical column
            # --------------------------------------------------

            elif is_object_dtype(series) or is_string_dtype(series):

                column_strategies[column] = (
                    ColumnCleaningStrategy(
                        strategy=CleaningStrategy.MODE,
                        reason="Categorical feature.",
                        missing_percentage=missing_percentage,
                    )
                )

                continue

            # --------------------------------------------------
            # Unknown datatype
            # --------------------------------------------------

            column_strategies[column] = (
                ColumnCleaningStrategy(
                    strategy=CleaningStrategy.NONE,
                    reason="Unsupported datatype.",
                    missing_percentage=missing_percentage,
                )
            )

        return CleaningPlan(
            column_strategies=column_strategies,
            columns_to_drop=columns_to_drop,
            remove_duplicates=self.config.remove_duplicates,
            trim_whitespace=self.config.trim_whitespace,
            datatype_conversions=datatype_conversions,
            notes=notes,
        )