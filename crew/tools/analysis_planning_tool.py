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
        "using the information already stored in the shared "
        "ProjectContext. "
        "IMPORTANT: This tool takes NO arguments. "
        "Do not provide target_column, problem_type, "
        "candidate_models, project_context, dataset, or any "
        "other arguments. "
        "The tool reads all required information directly "
        "from the shared ProjectContext."
    )

    analysis_planner: AIAnalysisPlanner = Field(
        default_factory=AIAnalysisPlanner,
    )

    def _run(self) -> str:

        context = ProjectContextManager.get_context()

        if context.dataset_info is None:
            raise ValueError(
                "Dataset metadata is missing from ProjectContext."
            )

        if context.data_quality is None:
            raise ValueError(
                "Data quality results are missing from ProjectContext."
            )

        if context.dataset_understanding is None:
            raise ValueError(
                "Dataset understanding is missing from ProjectContext."
            )

        if context.target_suggestion is None:
            raise ValueError(
                "Target identification is missing from ProjectContext. "
                "Run Target Identification first."
            )

        context.analysis_plan = (
            self.analysis_planner.create_plan(
                context,
            )
        )

        plan = context.analysis_plan

        if plan is None:
            raise ValueError(
                "Analysis planning returned no result."
            )

        return (
            "Analysis plan generated successfully.\n"
            f"Target Column: {plan.target_column}\n"
            f"Problem Type: {plan.problem_type.value}\n"
            f"Candidate Models: "
            f"{len(plan.candidate_models)}"
        )