from context.project_context import ProjectContext

from models.analysis_plan import AnalysisPlan

from prompts.templates.analysis_planning_prompt import (
    build_analysis_planning_prompt,
)

from services.ai.base_ai_service import BaseAIService


class AIAnalysisPlanner(BaseAIService):
    """
    Uses AI to create a machine learning analysis plan
    and validates the generated feature lists.
    """

    def create_plan(
        self,
        context: ProjectContext,
    ) -> AnalysisPlan:

        prompt = build_analysis_planning_prompt(
            context,
        )

        plan = self.generate_structured_output(
            prompt,
            AnalysisPlan,
        )

        # --------------------------------------------------
        # Validate target column to prevent data leakage
        # --------------------------------------------------

        target_column = plan.target_column

        plan.numerical_features = [
            column
            for column in plan.numerical_features
            if column != target_column
        ]

        plan.categorical_features = [
            column
            for column in plan.categorical_features
            if column != target_column
        ]

        return plan
