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


DatasetTool().run(
    dataset_path="datasets/employee_attrition.csv",
)

MetadataTool().run(
    file_name="datasets/employee_attrition.csv",
)

DataQualityTool().run()

CleaningStrategyTool().run()

DataCleaningTool().run()

result = DatasetUnderstandingTool().run()

print(result)

print("\n" + "=" * 60)
print("DATASET UNDERSTANDING")
print("=" * 60)

context = ProjectContextManager.get_context()

understanding = context.dataset_understanding

print(f"\nSummary:\n{understanding.summary}")

print(f"\nLikely Problem Type:")
print(understanding.likely_problem_type.value)

print("\nObservations:")

for observation in understanding.observations:
    print(f"- {observation}")