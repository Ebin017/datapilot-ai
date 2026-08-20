from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd

from context.project_context import ProjectContext
from models.eda_visualization import EDAVisualizationResult
from models.enums.problem_type import ProblemType

class EDAVisualizationService:
    """
    Generates EDA visualizations and saves them as images.
    """

    def __init__(self):
        self.output_dir = Path("outputs/charts")
        self.output_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

    def generate(
        self,
        context: ProjectContext,
    ) -> EDAVisualizationResult:
        """
        Generate all EDA visualizations.
        """

        chart_paths: list[str] = []

        ignored_columns = self._get_ignored_columns(
            context,
        )

        # histogram
        chart_paths.extend(
            self._generate_histograms(
                context.dataframe,
                ignored_columns,
            )
        )

        # boxplot
        chart_paths.extend(
            self._generate_boxplots(
                context.dataframe,
                ignored_columns,
            )
        )

        # heatmap
        chart_paths.extend(
            self._generate_correlation_heatmap(
                context.dataframe,
                ignored_columns,
            )
        )

        # count plot
        chart_paths.extend(
            self._generate_count_plots(
                context.dataframe,
                ignored_columns,
            )
        )

        # target distribution
        chart_paths.extend(
            self._generate_target_distribution(
                context,
            )
        )

        return EDAVisualizationResult(
            chart_paths=chart_paths,
        )

    def _get_ignored_columns(
        self,
        context: ProjectContext,
    ) -> set[str]:
        """
        Return columns that should not be visualized.
        """

        ignored_columns: set[str] = set()

        if context.analysis_plan is not None:
            ignored_columns.update(
                context.analysis_plan.columns_to_drop,
            )

        return ignored_columns

    def _generate_histograms(
        self,
        dataframe: pd.DataFrame,
        ignored_columns: set[str],
    ) -> list[str]:
        """
        Generate histogram for each numeric column.
        """

        chart_paths: list[str] = []

        numeric_columns = [
            column
            for column in dataframe.select_dtypes(
                include="number",
            ).columns
            if column not in ignored_columns
        ]

        for column in numeric_columns:

            plt.figure(figsize=(6, 4))

            dataframe[column].hist(
                bins="auto",
            )

            plt.title(f"{column} Distribution")
            plt.xlabel(column)
            plt.ylabel("Frequency")

            chart_path = (
                self.output_dir
                / f"{column.lower()}_histogram.png"
            )

            plt.tight_layout()

            plt.savefig(chart_path)

            plt.close()

            chart_paths.append(
                str(chart_path),
            )

        return chart_paths

    def _generate_boxplots(
        self,
        dataframe: pd.DataFrame,
        ignored_columns: set[str],
    ) -> list[str]:
        """
        Generate a boxplot for each numeric column.
        """

        chart_paths: list[str] = []

        numeric_columns = [
            column
            for column in dataframe.select_dtypes(
                include="number",
            ).columns
            if column not in ignored_columns
        ]

        for column in numeric_columns:

            plt.figure(figsize=(6, 4))

            plt.boxplot(
                dataframe[column].dropna(),
                vert=True,
            )

            plt.title(f"{column} Boxplot")
            plt.ylabel(column)

            chart_path = (
                self.output_dir
                / f"{column.lower()}_boxplot.png"
            )

            plt.tight_layout()

            plt.savefig(chart_path)

            plt.close()

            chart_paths.append(
                str(chart_path),
            )    

        return chart_paths

    def _generate_correlation_heatmap(
        self,
        dataframe: pd.DataFrame,
        ignored_columns: set[str],
    ) -> list[str]:
        """
        Generate a correlation heatmap for numeric features.
        """

        chart_paths: list[str] = []

        numeric_columns = [
            column
            for column in dataframe.select_dtypes(
                include="number",
            ).columns
            if column not in ignored_columns
        ]

        if len(numeric_columns) < 2:
            return chart_paths

        correlation_matrix = dataframe[
            numeric_columns
        ].corr()

        plt.figure(figsize=(8, 6))

        plt.imshow(
            correlation_matrix,
            cmap="coolwarm",
            interpolation="nearest",
        )

        plt.colorbar()

        plt.xticks(
            range(len(numeric_columns)),
            numeric_columns,
            rotation=45,
            ha="right",
        )

        plt.yticks(
            range(len(numeric_columns)),
            numeric_columns,
        )

        plt.title("Correlation Heatmap")

        plt.tight_layout()

        chart_path = (
            self.output_dir
            / "correlation_heatmap.png"
        )

        plt.savefig(chart_path)

        plt.close()

        chart_paths.append(
            str(chart_path),
        )

        return chart_paths

    # countplot
    def _generate_count_plots(
        self,
        dataframe: pd.DataFrame,
        ignored_columns: set[str],
    ) -> list[str]:
        """
        Generate count plots for categorical columns.
        """

        chart_paths: list[str] = []
        

        categorical_columns = [
            column
            for column in dataframe.select_dtypes(
                include=["object", "category", "bool"],
            ).columns
            if column not in ignored_columns
        ]

        for column in categorical_columns:

            if dataframe[column].nunique() > 20:
                continue

            counts = (
                dataframe[column]
                .value_counts(dropna=False)
            )

            plt.figure(figsize=(8, 5))

            plt.bar(
                counts.index.astype(str),
                counts.values,
            )

            plt.title(f"{column} Distribution")
            plt.xlabel(column)
            plt.ylabel("Count")

            plt.xticks(
                rotation=45,
                ha="right",
            )

            plt.tight_layout()

            chart_path = (
                self.output_dir
                / f"{column.lower()}_countplot.png"
            )

            plt.savefig(chart_path)

            plt.close()

            chart_paths.append(
                str(chart_path),
            )

        return chart_paths

    # target distribution
    def _generate_target_distribution(
        self,
        context: ProjectContext,
    ) -> list[str]:
        """
        Generate the target variable distribution.
        """

        chart_paths: list[str] = []

        if context.analysis_plan is None:
            return chart_paths

        target_column = context.analysis_plan.target_column

        if target_column not in context.dataframe.columns:
            return chart_paths

        plt.figure(figsize=(8, 5))

        if context.analysis_plan.problem_type == ProblemType.CLASSIFICATION:

            counts = (
                context.dataframe[target_column]
                .value_counts(dropna=False)
            )

            plt.bar(
                counts.index.astype(str),
                counts.values,
            )

            plt.ylabel("Count")

        else:

            context.dataframe[target_column].hist(
                bins="auto",
            )

            plt.ylabel("Frequency")

        plt.title(f"{target_column} Distribution")
        plt.xlabel(target_column)

        plt.xticks(
            rotation=45,
            ha="right",
        )

        plt.tight_layout()

        chart_path = (
            self.output_dir
            / "target_distribution.png"
        )

        plt.savefig(chart_path)

        plt.close()

        chart_paths.append(
            str(chart_path),
        )

        return chart_paths