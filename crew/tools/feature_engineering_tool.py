from pydantic import Field
from crewai.tools import BaseTool

from crew.context.project_context_manager import (
    ProjectContextManager,
)

from services.execution.feature_engineering.feature_engineering_service import (
    FeatureEngineeringService,
)


class FeatureEngineeringTool(BaseTool):
    """
    Performs feature engineering based on the analysis plan.
    """

    name: str = "Feature Engineering Tool"

    description: str = (
        "Prepare the cleaned dataset for machine learning using "
        "the AnalysisPlan stored in the shared ProjectContext. "
        "This includes encoding categorical variables, encoding "
        "the target when required, scaling numerical features, "
        "removing excluded columns, and separating features from "
        "the target. "
        "IMPORTANT: This tool takes NO arguments. "
        "Do not provide dataset, columns, target, analysis_plan, "
        "project_context, or any other arguments. "
        "The tool reads all required information directly from "
        "the shared ProjectContext."
    )

    feature_engineering_service: FeatureEngineeringService = Field(
        default_factory=FeatureEngineeringService,
    )

    def _run(self) -> str:

        context = ProjectContextManager.get_context()

        if context.analysis_plan is None:
            raise ValueError(
                "Analysis plan is missing from ProjectContext. "
                "Run Analysis Planning before Feature Engineering."
            )

        context.feature_engineering_result = (
            self.feature_engineering_service.transform(
                context,
            )
        )

        result = context.feature_engineering_result

        return (
            "Feature engineering completed successfully.\n"
            f"Features Shape: {result.features.shape}\n"
            f"Target Shape: {result.target.shape}\n"
            f"Total Features: {len(result.feature_names)}"
        )