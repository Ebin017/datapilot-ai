from context.project_context import ProjectContext

from models.target_suggestion import TargetSuggestion

from prompts.templates.target_identification_prompt import (
    build_target_identification_prompt,
)

from services.ai.base_ai_service import BaseAIService


class AITargetIdentificationService(BaseAIService):
    """
    Uses Gemini to identify the most likely prediction target.
    """

    def identify(
        self,
        context: ProjectContext,
    ) -> TargetSuggestion:

        prompt = build_target_identification_prompt(
            context,
        )

        return self.generate_structured_output(
            prompt,
            TargetSuggestion,
        )