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
        "Prepare the dataset for machine learning by "
        "encoding categorical variables, scaling numerical "
        "features and separating features from the target."
    )

    feature_engineering_service: FeatureEngineeringService = Field(
        default_factory=FeatureEngineeringService,
    )

    def _run(self) -> str:

        context = ProjectContextManager.get_context()

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