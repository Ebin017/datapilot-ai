from pydantic import Field
from crewai.tools import BaseTool

from crew.context.project_context_manager import (
    ProjectContextManager,
)

from services.explainability.explainability_service import (
    ExplainabilityService,
)


class ExplainabilityTool(BaseTool):
    """
    Generates SHAP explainability for the best trained model.
    """

    name: str = "Explainability Tool"

    description: str = (
        "Generate SHAP-based explanations and feature importance "
        "for the best trained machine learning model."
    )

    explainability_service: ExplainabilityService = Field(
        default_factory=ExplainabilityService,
    )

    def _run(self) -> str:

        context = ProjectContextManager.get_context()

        context.explainability_result = (
            self.explainability_service.explain(
                context,
            )
        )

        result = context.explainability_result

        return (
            "Explainability completed successfully.\n"
            f"Top Features: {len(result.top_features)}"
        )