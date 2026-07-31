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

result = TargetIdentificationTool().run()

print(result)

print("\n" + "=" * 60)
print("TARGET IDENTIFICATION")
print("=" * 60)

context = ProjectContextManager.get_context()

target = context.target_suggestion

print(f"\nTarget Column:")
print(target.column_name)

print(f"\nProblem Type:")
print(target.problem_type.value)

print(f"\nConfidence:")
print(target.confidence)

print(f"\nReason:")
print(target.reason)