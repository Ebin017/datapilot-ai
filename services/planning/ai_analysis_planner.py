from context.project_context import ProjectContext

from models.analysis_plan import AnalysisPlan

from prompts.templates.analysis_planning_prompt import (
    build_analysis_planning_prompt,
)

from services.ai.base_ai_service import BaseAIService


class AIAnalysisPlanner(BaseAIService):
    """
    Uses Gemini to create an analysis plan.
    """

    def create_plan(
        self,
        context: ProjectContext,
    ) -> AnalysisPlan:

        prompt = build_analysis_planning_prompt(
            context,
        )

        return self.generate_structured_output(
            prompt,
            AnalysisPlan,
        )