from pydantic import Field
from crewai.tools import BaseTool

from crew.context.project_context_manager import (
    ProjectContextManager,
)

from services.business_insight.business_insight_service import (
    BusinessInsightService,
)


class BusinessInsightTool(BaseTool):
    """
    Generates AI-powered business insights.
    """

    name: str = "Business Insight Tool"

    description: str = (
        "Generate executive-level business insights from the "
        "machine learning pipeline results."
    )

    business_insight_service: BusinessInsightService = Field(
        default_factory=BusinessInsightService,
    )

    def _run(
        self,
    ) -> str:

        context = ProjectContextManager.get_context()

        context.business_insight_result = (
            self.business_insight_service.generate(
                context,
            )
        )

        result = context.business_insight_result

        return (
            "Business insights generated successfully.\n"
            f"Executive Summary: {result.executive_summary[:100]}..."
        )