from context.project_context import ProjectContext

from models.dataset_understanding import DatasetUnderstanding

from prompts.templates.dataset_understanding_prompt import (
    build_dataset_understanding_prompt,
)

from services.ai.base_ai_service import BaseAIService


class DatasetUnderstandingService(BaseAIService):
    """
    Creates a high-level understanding of a dataset using Gemini.
    """

    def understand(
        self,
        context: ProjectContext,
    ) -> DatasetUnderstanding:

        prompt = build_dataset_understanding_prompt(
            context,
        )

        return self.generate_structured_output(
            prompt,
            DatasetUnderstanding,
        )