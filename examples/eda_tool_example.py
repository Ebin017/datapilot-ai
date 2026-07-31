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
from crew.tools.eda_tool import EDATool


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

AnalysisPlanningTool().run()

result = EDATool().run()

print(result)

print("\n" + "=" * 60)
print("EDA RESULT")
print("=" * 60)

context = ProjectContextManager.get_context()

eda = context.eda_result

print("\nNumerical Summary:")

for column, summary in eda.numerical_summary.items():
    print(f"\n{column}")
    for key, value in summary.items():
        print(f"  {key}: {value}")

print("\nCategorical Summary:")

for column, values in eda.categorical_summary.items():
    print(f"\n{column}")
    for key, value in values.items():
        print(f"  {key}: {value}")

print("\nCorrelation Matrix:")

for column, correlations in eda.correlation_matrix.items():
    print(f"\n{column}")
    for other_column, correlation in correlations.items():
        print(f"  {other_column}: {correlation}")

if eda.target_distribution:

    print("\nTarget Distribution:")

    for label, count in eda.target_distribution.items():
        print(f"  {label}: {count}")