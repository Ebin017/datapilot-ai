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

            dataset_understanding=(
                context.dataset_understanding.model_dump_json(
                    indent=2,
                )
            ),

            data_quality=(
                context.data_quality.model_dump_json(
                    indent=2,
                )
            ),

            eda=(
                context.eda_result.model_dump_json(
                    indent=2,
                )
            ),

            evaluation=(
                context.model_evaluation_result.model_dump_json(
                    indent=2,
                )
            ),

            explainability=(
                context.explainability_result.model_dump_json(
                    indent=2,
                )
            ),
        )

        return self.generate_structured_output(
            prompt,
            BusinessInsightResult,
        )