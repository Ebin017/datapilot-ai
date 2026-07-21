from models import BusinessInsightResult
from prompts.templates.business_insight_prompt import (
    BUSINESS_INSIGHT_PROMPT,
)
from services.ai.base_ai_service import BaseAIService


class BusinessInsightService(BaseAIService):
    """
    Generates business insights using the LLM.
    """

    def generate(
        self,
        context,
    ) -> BusinessInsightResult:

        prompt = BUSINESS_INSIGHT_PROMPT.format(
            dataset_understanding=context.dataset_understanding,
            data_quality=context.data_quality,
            eda=context.eda_result,
            evaluation=context.model_evaluation_result,
            top_features=context.explainability_result.top_features,
        )

        return self.generate_structured_output(
            prompt,
            BusinessInsightResult,
        )