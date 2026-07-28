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


DatasetTool().run(
    dataset_path="datasets/cleaning1.csv",
)

MetadataTool().run(
    file_name="datasets/cleaning1.csv",
)

DataQualityTool().run()

CleaningStrategyTool().run()

result = DataCleaningTool().run()

print(result)

print("\n" + "=" * 60)
print("DATA CLEANING SUMMARY")
print("=" * 60)

context = ProjectContextManager.get_context()

cleaning_result = context.data_cleaning_result

for summary in cleaning_result.cleaning_summary:
    print(f"- {summary}")

print("\nCurrent DataFrame Shape:")
print(context.dataframe.shape)