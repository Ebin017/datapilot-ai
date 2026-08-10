from pathlib import Path
from xml.sax.saxutils import escape

import matplotlib.pyplot as plt

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import (
    ParagraphStyle,
    getSampleStyleSheet,
)
from reportlab.lib.units import inch
from reportlab.platypus import (
    Image,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
    PageBreak,
)

from context.project_context import ProjectContext
from models.report_result import ReportResult


class ReportService:
    """
    Generates the final DataPilot AI PDF report.
    """

    def __init__(self):

        self.output_dir = Path(
            "outputs/reports"
        )

        self.output_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

    # ==================================================
    # Public method
    # ==================================================

    def generate(
        self,
        context: ProjectContext,
    ) -> ReportResult:

        report_path = (
            self.output_dir
            / "datapilot_report.pdf"
        )

        document = SimpleDocTemplate(
            str(report_path),
            pagesize=A4,
            rightMargin=40,
            leftMargin=40,
            topMargin=40,
            bottomMargin=40,
        )

        styles = getSampleStyleSheet()

        title_style = ParagraphStyle(
            "ReportTitle",
            parent=styles["Title"],
            alignment=TA_CENTER,
            spaceAfter=20,
        )

        heading_style = styles["Heading2"]

        subheading_style = styles["Heading3"]

        normal_style = styles["BodyText"]

        small_style = ParagraphStyle(
            "Small",
            parent=normal_style,
            fontSize=8,
            leading=10,
        )

        story = []

        # ==================================================
        # 1. TITLE
        # ==================================================

        story.append(
            Paragraph(
                "DataPilot AI - Data Science Report",
                title_style,
            )
        )

        story.append(
            Spacer(
                1,
                10,
            )
        )

        story.append(
            Paragraph(
                "Automated Machine Learning Analysis",
                normal_style,
            )
        )

        story.append(
            Spacer(
                1,
                20,
            )
        )

        # ==================================================
        # 2. DATASET OVERVIEW
        # ==================================================

        self._add_heading(
            story,
            "1. Dataset Overview",
            heading_style,
        )

        dataset_info = context.dataset_info

        dataset_table = Table(
            [
                ["File Name", dataset_info.file_name],
                ["Rows", str(dataset_info.rows)],
                ["Columns", str(dataset_info.columns)],
                [
                    "Numeric Columns",
                    str(
                        len(
                            dataset_info.numeric_columns or []
                        )
                    ),
                ],
                [
                    "Categorical Columns",
                    str(
                        len(
                            dataset_info.categorical_columns or []
                        )
                    ),
                ],
            ],
            colWidths=[
                180,
                270,
            ],
        )

        self._style_table(
            dataset_table,
        )

        story.append(dataset_table)

        story.append(
            Spacer(
                1,
                15,
            )
        )

        # ==================================================
        # 3. DATASET UNDERSTANDING
        # ==================================================

        if context.dataset_understanding:

            self._add_heading(
                story,
                "2. Dataset Understanding",
                heading_style,
            )

            understanding = (
                context.dataset_understanding
            )

            story.append(
                Paragraph(
                    f"<b>Summary:</b> "
                    f"{self._safe_text(understanding.summary)}",
                    normal_style,
                )
            )

            problem_type = (
                understanding.likely_problem_type
            )

            story.append(
                Paragraph(
                    f"<b>Problem Type:</b> "
                    f"{self._format_problem_type(problem_type)}",
                    normal_style,
                )
            )

            story.append(
                Spacer(
                    1,
                    8,
                )
            )

            story.append(
                Paragraph(
                    "<b>Observations:</b>",
                    normal_style,
                )
            )

            for observation in (
                understanding.observations
            ):

                story.append(
                    Paragraph(
                        f"• {self._safe_text(observation)}",
                        normal_style,
                    )
                )

            story.append(
                Spacer(
                    1,
                    15,
                )
            )

        # ==================================================
        # 4. DATA QUALITY
        # ==================================================

        if context.data_quality:

            self._add_heading(
                story,
                "3. Data Quality",
                heading_style,
            )

            quality = context.data_quality

            quality_table = Table(
                [
                    ["Metric", "Value"],
                    [
                        "Duplicate Rows",
                        str(
                            quality.duplicate_rows
                        ),
                    ],
                    [
                        "Duplicate Percentage",
                        f"{quality.duplicate_percentage:.2f}%",
                    ],
                    [
                        "Constant Columns",
                        str(
                            len(
                                quality.constant_columns
                            )
                        ),
                    ],
                    [
                        "Empty Columns",
                        str(
                            len(
                                quality.empty_columns
                            )
                        ),
                    ],
                ],
                colWidths=[
                    250,
                    200,
                ],
            )

            self._style_table(
                quality_table,
            )

            story.append(quality_table)

            story.append(
                Spacer(
                    1,
                    15,
                )
            )

        # ==================================================
        # 5. DATA CLEANING
        # ==================================================

        if context.data_cleaning_result:

            self._add_heading(
                story,
                "4. Data Cleaning",
                heading_style,
            )

            cleaning = (
                context.data_cleaning_result
            )

            cleaning_table = Table(
                [
                    ["Metric", "Value"],
                    [
                        "Original Rows",
                        str(
                            cleaning.original_rows
                        ),
                    ],
                    [
                        "Final Rows",
                        str(
                            cleaning.final_rows
                        ),
                    ],
                    [
                        "Duplicate Rows Removed",
                        str(
                            cleaning.duplicate_rows_removed
                        ),
                    ],
                    [
                        "Columns Removed",
                        str(
                            len(
                                cleaning.columns_removed
                            )
                        ),
                    ],
                    [
                        "Missing Value Columns Handled",
                        str(
                            len(
                                cleaning.missing_values_filled
                            )
                        ),
                    ],
                ],
                colWidths=[
                    250,
                    200,
                ],
            )

            self._style_table(
                cleaning_table,
            )

            story.append(cleaning_table)

            story.append(
                Spacer(
                    1,
                    10,
                )
            )

            if cleaning.cleaning_summary:

                story.append(
                    Paragraph(
                        "<b>Cleaning Summary:</b>",
                        normal_style,
                    )
                )

                for item in (
                    cleaning.cleaning_summary
                ):

                    story.append(
                        Paragraph(
                            f"• {self._safe_text(item)}",
                            normal_style,
                        )
                    )

            story.append(
                Spacer(
                    1,
                    15,
                )
            )

        # ==================================================
        # 6. ANALYSIS PLAN
        # ==================================================

        if context.analysis_plan:

            self._add_heading(
                story,
                "5. Analysis Plan",
                heading_style,
            )

            plan = context.analysis_plan

            plan_table = Table(
                [
                    [
                        "Target Column",
                        plan.target_column,
                    ],
                    [
                        "Problem Type",
                        self._format_problem_type(
                            plan.problem_type
                        ),
                    ],
                    [
                        "Evaluation Metric",
                        plan.evaluation_metric,
                    ],
                    [
                        "Train/Test Split",
                        str(
                            plan.train_test_split
                        ),
                    ],
                    [
                        "Random State",
                        str(
                            plan.random_state
                        ),
                    ],
                    [
                        "Scaling",
                        str(
                            plan.scaling_method
                        ),
                    ],
                    [
                        "Feature Encoding",
                        str(
                            plan.feature_encoding
                        ),
                    ],
                    [
                        "Target Encoding",
                        str(
                            plan.target_encoding
                        ),
                    ],
                ],
                colWidths=[
                    200,
                    250,
                ],
            )

            self._style_table(
                plan_table,
            )

            story.append(plan_table)

            story.append(
                Spacer(
                    1,
                    10,
                )
            )

            story.append(
                Paragraph(
                    "<b>Numerical Features:</b> "
                    + self._safe_text(
                        ", ".join(
                            plan.numerical_features
                        )
                    ),
                    small_style,
                )
            )

            story.append(
                Paragraph(
                    "<b>Categorical Features:</b> "
                    + self._safe_text(
                        ", ".join(
                            plan.categorical_features
                        )
                    ),
                    small_style,
                )
            )

            story.append(
                Spacer(
                    1,
                    15,
                )
            )

        # ==================================================
        # 7. EDA
        # ==================================================

        if context.eda_result:

            self._add_heading(
                story,
                "6. Exploratory Data Analysis",
                heading_style,
            )

            eda = context.eda_result

            # Numerical summary

            if eda.numerical_summary:

                story.append(
                    Paragraph(
                        "<b>Numerical Summary</b>",
                        subheading_style,
                    )
                )

                for column, values in (
                    eda.numerical_summary.items()
                ):

                    story.append(
                        Paragraph(
                            f"<b>{self._safe_text(column)}</b>",
                            normal_style,
                        )
                    )

                    table_data = [
                        ["Statistic", "Value"]
                    ]

                    for key, value in values.items():

                        try:
                            formatted = f"{float(value):.3f}"
                        except (
                            ValueError,
                            TypeError,
                        ):
                            formatted = str(value)

                        table_data.append(
                            [
                                key,
                                formatted,
                            ]
                        )

                    table = Table(
                        table_data,
                        colWidths=[
                            200,
                            150,
                        ],
                    )

                    self._style_table(
                        table,
                    )

                    story.append(table)

                    story.append(
                        Spacer(
                            1,
                            8,
                        )
                    )

            # Categorical summary

            if eda.categorical_summary:

                story.append(
                    Paragraph(
                        "<b>Categorical Summary</b>",
                        subheading_style,
                    )
                )

                for column, values in (
                    eda.categorical_summary.items()
                ):

                    story.append(
                        Paragraph(
                            f"<b>{self._safe_text(column)}</b>",
                            normal_style,
                        )
                    )

                    table_data = [
                        ["Category", "Count"]
                    ]

                    for category, count in (
                        values.items()
                    ):

                        table_data.append(
                            [
                                str(category),
                                str(count),
                            ]
                        )

                    table = Table(
                        table_data,
                        colWidths=[
                            200,
                            150,
                        ],
                    )

                    self._style_table(
                        table,
                    )

                    story.append(table)

                    story.append(
                        Spacer(
                            1,
                            8,
                        )
                    )

            # Target distribution

            if eda.target_distribution:

                story.append(
                    Paragraph(
                        "<b>Target Distribution</b>",
                        subheading_style,
                    )
                )

                target_data = [
                    ["Target", "Count"]
                ]

                for value, count in (
                    eda.target_distribution.items()
                ):

                    target_data.append(
                        [
                            str(value),
                            str(count),
                        ]
                    )

                target_table = Table(
                    target_data,
                    colWidths=[
                        200,
                        150,
                    ],
                )

                self._style_table(
                    target_table,
                )

                story.append(target_table)

            story.append(
                Spacer(
                    1,
                    15,
                )
            )

        # ==================================================
        # 8. EDA VISUALIZATIONS
        # ==================================================

        if context.eda_visualization_result:

            chart_paths = (
                context
                .eda_visualization_result
                .chart_paths
            )

            if chart_paths:

                self._add_heading(
                    story,
                    "7. EDA Visualizations",
                    heading_style,
                )

                for chart_path in chart_paths:

                    path = Path(chart_path)

                    if not path.exists():
                        continue

                    story.append(
                        Paragraph(
                            self._safe_text(
                                path.stem.replace(
                                    "_",
                                    " ",
                                ).title()
                            ),
                            subheading_style,
                        )
                    )

                    try:

                        image = Image(
                            str(path),
                            width=5.8 * inch,
                            height=3.6 * inch,
                        )

                        story.append(image)

                        story.append(
                            Spacer(
                                1,
                                10,
                            )
                        )

                    except Exception:

                        story.append(
                            Paragraph(
                                f"Unable to load chart: "
                                f"{self._safe_text(str(path))}",
                                small_style,
                            )
                        )

        # ==================================================
        # 9. FEATURE ENGINEERING
        # ==================================================

        if context.feature_engineering_result:

            self._add_heading(
                story,
                "8. Feature Engineering",
                heading_style,
            )

            feature_result = (
                context.feature_engineering_result
            )

            story.append(
                Paragraph(
                    f"<b>Total Features:</b> "
                    f"{len(feature_result.feature_names)}",
                    normal_style,
                )
            )

            story.append(
                Paragraph(
                    f"<b>Feature Matrix Shape:</b> "
                    f"{feature_result.features.shape}",
                    normal_style,
                )
            )

            story.append(
                Paragraph(
                    "<b>Generated Features:</b>",
                    normal_style,
                )
            )

            for feature in (
                feature_result.feature_names
            ):

                story.append(
                    Paragraph(
                        f"• {self._safe_text(feature)}",
                        small_style,
                    )
                )

            story.append(
                Spacer(
                    1,
                    15,
                )
            )

        # ==================================================
        # 10. MODEL TRAINING
        # ==================================================

        if context.model_training_result:

            self._add_heading(
                story,
                "9. Model Training",
                heading_style,
            )

            training = (
                context.model_training_result
            )

            training_table = Table(
                [
                    ["Model", "Score"],
                    *[
                        [
                            name,
                            f"{score:.4f}",
                        ]
                        for name, score in (
                            training.evaluation_scores.items()
                        )
                    ],
                ],
                colWidths=[
                    250,
                    200,
                ],
            )

            self._style_table(
                training_table,
            )

            story.append(training_table)

            story.append(
                Spacer(
                    1,
                    10,
                )
            )

            story.append(
                Paragraph(
                    f"<b>Best Model:</b> "
                    f"{self._safe_text(training.best_model_name)}",
                    normal_style,
                )
            )

            story.append(
                Paragraph(
                    f"<b>Best Score:</b> "
                    f"{training.best_score:.4f}",
                    normal_style,
                )
            )

            story.append(
                Paragraph(
                    f"<b>Training Samples:</b> "
                    f"{len(training.x_train)}",
                    normal_style,
                )
            )

            story.append(
                Paragraph(
                    f"<b>Testing Samples:</b> "
                    f"{len(training.x_test)}",
                    normal_style,
                )
            )

            story.append(
                Spacer(
                    1,
                    15,
                )
            )

        # ==================================================
        # 11. MODEL EVALUATION
        # ==================================================

        if context.model_evaluation_result:

            self._add_heading(
                story,
                "10. Model Evaluation",
                heading_style,
            )

            evaluation = (
                context.model_evaluation_result
            )

            evaluation_data = [
                ["Metric", "Value"]
            ]

            for metric, value in (
                evaluation.metrics.items()
            ):

                evaluation_data.append(
                    [
                        metric,
                        f"{value:.4f}",
                    ]
                )

            evaluation_table = Table(
                evaluation_data,
                colWidths=[
                    250,
                    200,
                ],
            )

            self._style_table(
                evaluation_table,
            )

            story.append(
                evaluation_table
            )

            # Confusion matrix

            if evaluation.confusion_matrix:

                story.append(
                    Spacer(
                        1,
                        10,
                    )
                )

                story.append(
                    Paragraph(
                        "<b>Confusion Matrix</b>",
                        subheading_style,
                    )
                )

                matrix_data = [
                    [
                        "Actual / Predicted"
                    ]
                    + [
                        str(index)
                        for index in range(
                            len(
                                evaluation.confusion_matrix
                            )
                        )
                    ]
                ]

                for index, row in enumerate(
                    evaluation.confusion_matrix
                ):

                    matrix_data.append(
                        [
                            str(index)
                        ]
                        + [
                            str(value)
                            for value in row
                        ]
                    )

                matrix_table = Table(
                    matrix_data,
                )

                self._style_table(
                    matrix_table,
                )

                story.append(
                    matrix_table
                )

            story.append(
                Spacer(
                    1,
                    15,
                )
            )

        # ==================================================
        # 12. EXPLAINABILITY
        # ==================================================

        if context.explainability_result:

            self._add_heading(
                story,
                "11. Model Explainability",
                heading_style,
            )

            explainability = (
                context.explainability_result
            )

            story.append(
                Paragraph(
                    "<b>Top Features</b>",
                    subheading_style,
                )
            )

            importance_data = [
                [
                    "Feature",
                    "Importance",
                ]
            ]

            for feature in (
                explainability.top_features
            ):

                importance = (
                    explainability.feature_importance[
                        feature
                    ]
                )

                importance_data.append(
                    [
                        self._safe_text(feature),
                        f"{importance:.4f}",
                    ]
                )

            importance_table = Table(
                importance_data,
                colWidths=[
                    250,
                    200,
                ],
            )

            self._style_table(
                importance_table,
            )

            story.append(
                importance_table
            )

            story.append(
                Spacer(
                    1,
                    15,
                )
            )

            # SHAP feature importance chart

            shap_chart = (
                self._generate_shap_chart(
                    explainability,
                )
            )

            if shap_chart:

                story.append(
                    Paragraph(
                        "<b>SHAP Feature Importance</b>",
                        subheading_style,
                    )
                )

                story.append(
                    Image(
                        str(shap_chart),
                        width=6.0 * inch,
                        height=4.0 * inch,
                    )
                )

                story.append(
                    Spacer(
                        1,
                        15,
                    )
                )

        # ==================================================
        # 13. BUSINESS INSIGHTS
        # ==================================================

        if context.business_insight_result:

            self._add_heading(
                story,
                "12. Business Insights",
                heading_style,
            )

            insights = (
                context.business_insight_result
            )

            self._add_paragraph_section(
                story,
                "Executive Summary",
                insights.executive_summary,
                subheading_style,
                normal_style,
            )

            self._add_list_section(
                story,
                "Key Findings",
                insights.key_findings,
                subheading_style,
                normal_style,
            )

            self._add_paragraph_section(
                story,
                "Model Performance Summary",
                insights.model_performance_summary,
                subheading_style,
                normal_style,
            )

            self._add_paragraph_section(
                story,
                "Feature Importance Summary",
                insights.feature_importance_summary,
                subheading_style,
                normal_style,
            )

            self._add_list_section(
                story,
                "Business Recommendations",
                insights.business_recommendations,
                subheading_style,
                normal_style,
            )

            self._add_list_section(
                story,
                "Risks and Limitations",
                insights.risks_and_limitations,
                subheading_style,
                normal_style,
            )

            self._add_list_section(
                story,
                "Next Steps",
                insights.next_steps,
                subheading_style,
                normal_style,
            )

        # ==================================================
        # BUILD PDF
        # ==================================================

        document.build(
            story,
        )

        return ReportResult(
            report_path=str(report_path),
            report_title=(
                "DataPilot AI - Data Science Report"
            ),
        )

    # ==================================================
    # Helper methods
    # ==================================================

    @staticmethod
    def _add_heading(
        story,
        text,
        style,
    ):

        story.append(
            Paragraph(
                text,
                style,
            )
        )

        story.append(
            Spacer(
                1,
                8,
            )
        )

    @staticmethod
    def _style_table(
        table,
    ):

        table.setStyle(
            TableStyle(
                [
                    (
                        "BACKGROUND",
                        (0, 0),
                        (-1, 0),
                        colors.lightgrey,
                    ),
                    (
                        "GRID",
                        (0, 0),
                        (-1, -1),
                        0.5,
                        colors.grey,
                    ),
                    (
                        "VALIGN",
                        (0, 0),
                        (-1, -1),
                        "TOP",
                    ),
                    (
                        "LEFTPADDING",
                        (0, 0),
                        (-1, -1),
                        6,
                    ),
                    (
                        "RIGHTPADDING",
                        (0, 0),
                        (-1, -1),
                        6,
                    ),
                    (
                        "TOPPADDING",
                        (0, 0),
                        (-1, -1),
                        5,
                    ),
                    (
                        "BOTTOMPADDING",
                        (0, 0),
                        (-1, -1),
                        5,
                    ),
                ]
            )
        )

    @staticmethod
    def _safe_text(
        value,
    ) -> str:

        return escape(
            str(value)
        )

    @staticmethod
    def _format_problem_type(
        problem_type,
    ) -> str:

        value = getattr(
            problem_type,
            "value",
            problem_type,
        )

        return str(
            value
        ).replace(
            "_",
            " ",
        ).title()

    @staticmethod
    def _add_paragraph_section(
        story,
        title,
        text,
        heading_style,
        normal_style,
    ):

        story.append(
            Paragraph(
                f"<b>{title}</b>",
                heading_style,
            )
        )

        story.append(
            Paragraph(
                ReportService._safe_text(
                    text
                ),
                normal_style,
            )
        )

        story.append(
            Spacer(
                1,
                10,
            )
        )

    @staticmethod
    def _add_list_section(
        story,
        title,
        items,
        heading_style,
        normal_style,
    ):

        story.append(
            Paragraph(
                f"<b>{title}</b>",
                heading_style,
            )
        )

        for item in items:

            story.append(
                Paragraph(
                    f"• "
                    f"{ReportService._safe_text(item)}",
                    normal_style,
                )
            )

        story.append(
            Spacer(
                1,
                10,
            )
        )

    def _generate_shap_chart(
        self,
        explainability,
    ) -> Path | None:
        """
        Generate a SHAP feature-importance chart.
        """

        if not explainability.feature_importance:
            return None

        chart_path = (
            self.output_dir
            / "shap_feature_importance.png"
        )

        features = list(
            explainability.feature_importance.keys()
        )[:10]

        values = [
            explainability.feature_importance[
                feature
            ]
            for feature in features
        ]

        # Reverse for horizontal bar chart
        features = features[::-1]
        values = values[::-1]

        plt.figure(
            figsize=(8, 5),
        )

        plt.barh(
            features,
            values,
        )

        plt.xlabel(
            "Mean Absolute SHAP Value"
        )

        plt.title(
            "Top SHAP Feature Importance"
        )

        plt.tight_layout()

        plt.savefig(
            chart_path,
            dpi=150,
        )

        plt.close()

        return chart_path