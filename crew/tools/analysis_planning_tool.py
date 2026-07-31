from pydantic import Field
from crewai.tools import BaseTool

from crew.context.project_context_manager import (
    ProjectContextManager,
)
from services.planning.ai_analysis_planner import (
    AIAnalysisPlanner,
)


class AnalysisPlanningTool(BaseTool):
    """
    Generates an AI-powered machine learning analysis plan.
    """

    name: str = "Analysis Planning Tool"

    description: str = (
        "Generate a complete machine learning analysis plan "
        "including target column, preprocessing strategy, "
        "evaluation metric and candidate models."
    )

    analysis_planner: AIAnalysisPlanner = Field(
        default_factory=AIAnalysisPlanner,
    )

    def _run(self) -> str:

        context = ProjectContextManager.get_context()

        context.analysis_plan = (
            self.analysis_planner.create_plan(
                context,
            )
        )

        plan = context.analysis_plan

        return (
            "Analysis plan generated successfully.\n"
            f"Target Column: {plan.target_column}\n"
            f"Problem Type: {plan.problem_type.value}\n"
            f"Candidate Models: {len(plan.candidate_models)}"
        )