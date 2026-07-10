from context.project_context import ProjectContext
from models.analysis_plan import AnalysisPlan


class AnalysisPlanner:
    """
    Creates an analysis plan from the current project context.
    """

    def create_plan(
        self,
        context: ProjectContext,
    ) -> AnalysisPlan:
        
        if context.target_suggestion is None:
            raise ValueError(
                "Target suggestion is required before creating an analysis plan."
            )

        preprocessing_steps = []

        total_missing = sum(
            context.data_quality.missing_values.values()
        )

        if total_missing > 0:
            preprocessing_steps.append(
                "Handle missing values"
            )

        if context.dataset_info.categorical_columns:
            preprocessing_steps.append(
                "Encode categorical variables"
            )

        preprocessing_steps.append(
            "Split features and target"
        )

        return AnalysisPlan(
            target_column=context.target_suggestion.column_name,
            problem_type=context.target_suggestion.problem_type,
            evaluation_metric="f1_score",
            train_test_split=0.2,
            random_state=42,
            stratify_split=True,
            preprocessing_steps=preprocessing_steps,
        )