from context.project_context import ProjectContext
from models.enums.problem_type import ProblemType
from models.target_suggestion import TargetSuggestion


class RuleBasedTargetIdentificationService:
    """
    Identifies the most likely prediction target column.
    """

    TARGET_KEYWORDS = {
        "target",
        "label",
        "class",
        "churn",
        "exited",
        "default",
        "fraud",
        "survived",
    }

    ID_COLUMNS = {
        "id",
        "customerid",
        "customer_id",
        "employeeid",
        "employee_id",
        "userid",
        "user_id",
        "orderid",
        "order_id",
    }

    def identify(
        self,
        context: ProjectContext,
    ) -> TargetSuggestion:
        """
        Identify the most likely prediction target.
        """

        suggestion = self._find_keyword_match(context)
        if suggestion:
            return suggestion

        suggestion = self._find_binary_target(context)
        if suggestion:
            return suggestion

        return self._fallback_target(context)

    def _find_keyword_match(
        self,
        context: ProjectContext,
    ) -> TargetSuggestion | None:
        """
        Look for well-known target column names.
        """

        for column in context.dataset_info.categorical_columns:

            if column.lower() in self.TARGET_KEYWORDS:

                return TargetSuggestion(
                    column_name=column,
                    problem_type=ProblemType.CLASSIFICATION,
                    confidence=0.95,
                    reason=(
                        "The column name strongly suggests it is the prediction target."
                    ),
                )

        return None

    def _find_binary_target(
        self,
        context: ProjectContext,
    ) -> TargetSuggestion | None:
        """
        Look for binary categorical columns.
        """

        dataframe = context.dataframe

        for column in context.dataset_info.categorical_columns:

            if column.lower() in self.ID_COLUMNS:
                continue

            unique_values = dataframe[column].dropna().unique()

            if len(unique_values) == 2:

                return TargetSuggestion(
                    column_name=column,
                    problem_type=ProblemType.CLASSIFICATION,
                    confidence=0.85,
                    reason=(
                        "The column is binary, making it a strong candidate "
                        "for a classification target."
                    ),
                )

        return None

    def _fallback_target(
        self,
        context: ProjectContext,
    ) -> TargetSuggestion:
        """
        Fallback strategy when no better candidate is found.
        """

        categorical_columns = context.dataset_info.categorical_columns

        if not categorical_columns:
            raise ValueError(
                "No categorical columns were found in the dataset."
            )

        return TargetSuggestion(
            column_name=categorical_columns[-1],
            problem_type=ProblemType.CLASSIFICATION,
            confidence=0.60,
            reason=(
                "Using the last categorical column as a fallback target."
            ),
        )