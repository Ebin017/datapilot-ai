import pandas as pd

from context.project_context import ProjectContext
from models.eda_result import EDAResult
from models.enums.problem_type import ProblemType


class ExploratoryDataAnalysisService:
    """
    Performs exploratory data analysis based on the analysis plan.
    """

    def analyze(
        self,
        context: ProjectContext,
    ) -> EDAResult:

        dataframe = context.dataframe

        return EDAResult(
            numerical_summary=self._numerical_summary(
                dataframe,
                context,
            ),
            categorical_summary=self._categorical_summary(
                dataframe,
                context,
            ),
            correlation_matrix=self._correlation_matrix(
                dataframe,
                context,
            ),
            target_distribution=self._target_distribution(
                dataframe,
                context,
            ),
        )

    def _numerical_summary(
        self,
        dataframe: pd.DataFrame,
        context: ProjectContext,
    ) -> dict[str, dict]:

        columns = context.analysis_plan.numerical_features

        if not columns:
            return {}

        return (
            dataframe[columns]
            .describe()
            .round(3)
            .to_dict()
        )

    def _categorical_summary(
        self,
        dataframe: pd.DataFrame,
        context: ProjectContext,
    ) -> dict[str, dict]:

        summary = {}

        for column in context.analysis_plan.categorical_features:
            summary[column] = (
                dataframe[column]
                .value_counts(dropna=False)
                .to_dict()
            )

        return summary

    def _correlation_matrix(
        self,
        dataframe: pd.DataFrame,
        context: ProjectContext,
    ) -> dict[str, dict]:

        columns = context.analysis_plan.numerical_features

        if len(columns) < 2:
            return {}

        return (
            dataframe[columns]
            .corr()
            .round(3)
            .to_dict()
        )

    def _target_distribution(
        self,
        dataframe: pd.DataFrame,
        context: ProjectContext,
    ) -> dict[str, int] | None:

        if (
            context.analysis_plan.problem_type
            != ProblemType.CLASSIFICATION
        ):
            return None

        target = context.analysis_plan.target_column

        return (
            dataframe[target]
            .value_counts(dropna=False)
            .to_dict()
        )