from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)

from context.project_context import ProjectContext
from models.report_result import ReportResult


class ReportService:
    """
    Generates the final DataPilot PDF report.
    """

    def __init__(self):

        self.output_dir = Path("outputs/reports")

        self.output_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

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

        title_style = styles["Title"]
        heading_style = styles["Heading2"]
        normal_style = styles["BodyText"]

        story = []

        # --------------------------------------------------
        # Title
        # --------------------------------------------------

        story.append(
            Paragraph(
                "DataPilot AI - Data Science Report",
                title_style,
            )
        )

        story.append(
            Spacer(
                1,
                20,
            )
        )

        # --------------------------------------------------
        # Dataset Overview
        # --------------------------------------------------

        story.append(
            Paragraph(
                "1. Dataset Overview",
                heading_style,
            )
        )

        dataset_info = context.dataset_info

        dataset_table = Table(
            [
                ["File Name", dataset_info.file_name],
                ["Rows", str(dataset_info.rows)],
                ["Columns", str(dataset_info.columns)],
            ],
            colWidths=[
                150,
                300,
            ],
        )

        dataset_table.setStyle(
            TableStyle(
                [
                    (
                        "BACKGROUND",
                        (0, 0),
                        (0, -1),
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
                ]
            )
        )

        story.append(dataset_table)

        story.append(
            Spacer(
                1,
                15,
            )
        )

        # --------------------------------------------------
        # Dataset Understanding
        # --------------------------------------------------

        if context.dataset_understanding:

            story.append(
                Paragraph(
                    "2. Dataset Understanding",
                    heading_style,
                )
            )

            understanding = (
                context.dataset_understanding
            )

            story.append(
                Paragraph(
                    f"<b>Summary:</b> "
                    f"{understanding.summary}",
                    normal_style,
                )
            )

            story.append(
                Paragraph(
                    f"<b>Problem Type:</b> "
                    f"{understanding.likely_problem_type}",
                    normal_style,
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
                    "<b>Observations:</b>",
                    normal_style,
                )
            )

            for observation in understanding.observations:

                story.append(
                    Paragraph(
                        f"- {observation}",
                        normal_style,
                    )
                )

            story.append(
                Spacer(
                    1,
                    15,
                )
            )

        # --------------------------------------------------
        # Data Quality
        # --------------------------------------------------

        if context.data_quality:

            story.append(
                Paragraph(
                    "3. Data Quality",
                    heading_style,
                )
            )

            quality = context.data_quality

            quality_table = Table(
                [
                    [
                        "Metric",
                        "Value",
                    ],
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

            quality_table.setStyle(
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
                    ]
                )
            )

            story.append(
                quality_table
            )

            story.append(
                Spacer(
                    1,
                    15,
                )
            )

        # --------------------------------------------------
        # Model Evaluation
        # --------------------------------------------------

        if context.model_evaluation_result:

            story.append(
                Paragraph(
                    "4. Model Evaluation",
                    heading_style,
                )
            )

            evaluation = (
                context.model_evaluation_result
            )

            evaluation_data = [
                [
                    "Metric",
                    "Value",
                ]
            ]

            for metric, value in evaluation.metrics.items():

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

            evaluation_table.setStyle(
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
                    ]
                )
            )

            story.append(
                evaluation_table
            )

            story.append(
                Spacer(
                    1,
                    15,
                )
            )

        # --------------------------------------------------
        # Explainability
        # --------------------------------------------------

        if context.explainability_result:

            story.append(
                Paragraph(
                    "5. Model Explainability",
                    heading_style,
                )
            )

            explainability = (
                context.explainability_result
            )

            story.append(
                Paragraph(
                    "<b>Top Features:</b>",
                    normal_style,
                )
            )

            for feature in explainability.top_features:

                importance = (
                    explainability.feature_importance[
                        feature
                    ]
                )

                story.append(
                    Paragraph(
                        f"- {feature}: "
                        f"{importance:.4f}",
                        normal_style,
                    )
                )

            story.append(
                Spacer(
                    1,
                    15,
                )
            )

        # --------------------------------------------------
        # Business Insights
        # --------------------------------------------------

        if context.business_insight_result:

            story.append(
                Paragraph(
                    "6. Business Insights",
                    heading_style,
                )
            )

            insights = (
                context.business_insight_result
            )

            story.append(
                Paragraph(
                    "<b>Executive Summary</b>",
                    normal_style,
                )
            )

            story.append(
                Paragraph(
                    insights.executive_summary,
                    normal_style,
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
                    "<b>Key Findings</b>",
                    normal_style,
                )
            )

            for finding in insights.key_findings:

                story.append(
                    Paragraph(
                        f"- {finding}",
                        normal_style,
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
                    "<b>Recommendations</b>",
                    normal_style,
                )
            )

            for recommendation in (
                insights.business_recommendations
            ):

                story.append(
                    Paragraph(
                        f"- {recommendation}",
                        normal_style,
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
                    "<b>Risks and Limitations</b>",
                    normal_style,
                )
            )

            for risk in insights.risks_and_limitations:

                story.append(
                    Paragraph(
                        f"- {risk}",
                        normal_style,
                    )
                )

        # --------------------------------------------------
        # Build PDF
        # --------------------------------------------------

        document.build(story)

        return ReportResult(
            report_path=str(report_path),
            report_title="DataPilot AI - Data Science Report",
        )