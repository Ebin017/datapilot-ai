from pydantic import BaseModel


class BusinessInsightResult(BaseModel):
    """
    AI-generated business insights.
    """

    executive_summary: str

    key_findings: list[str]

    model_performance_summary: str

    feature_importance_summary: str

    business_recommendations: list[str]

    risks_and_limitations: list[str]

    next_steps: list[str]