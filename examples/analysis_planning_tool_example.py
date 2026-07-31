from crew.context.project_context_manager import (
    ProjectContextManager,
)

from crew.tools.dataset_tool import DatasetTool
from crew.tools.metadata_tool import MetadataTool
from crew.tools.data_quality_tool import DataQualityTool
from crew.tools.cleaning_strategy_tool import (
    CleaningStrategyTool,
)
from crew.tools.data_cleaning_tool import (
    DataCleaningTool,
)
from crew.tools.dataset_understanding_tool import (
    DatasetUnderstandingTool,
)
from crew.tools.target_identification_tool import (
    TargetIdentificationTool,
)
from crew.tools.analysis_planning_tool import (
    AnalysisPlanningTool,
)


DatasetTool().run(
    dataset_path="datasets/employee_attrition.csv",
)

MetadataTool().run(
    file_name="datasets/employee_attrition.csv",
)

DataQualityTool().run()

CleaningStrategyTool().run()

DataCleaningTool().run()

DatasetUnderstandingTool().run()

TargetIdentificationTool().run()

result = AnalysisPlanningTool().run()

print(result)

print("\n" + "=" * 60)
print("ANALYSIS PLAN")
print("=" * 60)

context = ProjectContextManager.get_context()

plan = context.analysis_plan

print(f"\nTarget Column:")
print(plan.target_column)

print(f"\nProblem Type:")
print(plan.problem_type.value)

print(f"\nEvaluation Metric:")
print(plan.evaluation_metric)

print(f"\nTrain/Test Split:")
print(plan.train_test_split)

print(f"\nRandom State:")
print(plan.random_state)

print(f"\nStratify Split:")
print(plan.stratify_split)

print(f"\nColumns to Drop:")
print(plan.columns_to_drop)

print(f"\nNumerical Features:")
print(plan.numerical_features)

print(f"\nCategorical Features:")
print(plan.categorical_features)

print(f"\nScaling Method:")
print(plan.scaling_method)

print(f"\nFeature Encoding:")
print(plan.feature_encoding)

print(f"\nTarget Encoding:")
print(plan.target_encoding)

print("\nCandidate Models:")

for model in plan.candidate_models:
    print(f"- {model.name}")