from context.project_context import ProjectContext
from models.dataset_understanding import DatasetUnderstanding
from models.enums.problem_type import ProblemType


class DatasetUnderstandingService:
    """
    Creates a high-level understanding of the dataset.
    """

    def understand(
        self,
        context: ProjectContext,
    ) -> DatasetUnderstanding:

        observations: list[str] = []

        dataset_info = context.dataset_info
        data_quality = context.data_quality

        # Feature types
        if (
            dataset_info.numeric_columns
            and dataset_info.categorical_columns
        ):
            observations.append(
                "The dataset contains both numeric and categorical features."
            )

        elif dataset_info.numeric_columns:
            observations.append(
                "The dataset contains only numeric features."
            )

        elif dataset_info.categorical_columns:
            observations.append(
                "The dataset contains only categorical features."
            )

        # Missing values
        total_missing = sum(data_quality.missing_values.values())

        if total_missing == 0:
            observations.append(
                "No missing values were detected."
            )
        else:
            observations.append(
                f"The dataset contains {total_missing} missing values."
            )

        # Duplicate rows
        if data_quality.duplicate_rows == 0:
            observations.append(
                "No duplicate rows were found."
            )
        else:
            observations.append(
                f"The dataset contains {data_quality.duplicate_rows} duplicate rows."
            )

        # Ready for modelling
        if (
            total_missing == 0
            and data_quality.duplicate_rows == 0
        ):
            observations.append(
                "The dataset appears ready for modeling."
            )

        return DatasetUnderstanding(
            summary=(
                f"The dataset contains "
                f"{dataset_info.rows:,} rows and "
                f"{dataset_info.columns} columns."
            ),
            likely_problem_type=ProblemType.CLASSIFICATION,
            observations=observations,
        )