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
from crew.tools.eda_visualization_tool import (
    EDAVisualizationTool,
)
from crew.tools.feature_engineering_tool import (
    FeatureEngineeringTool,
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

AnalysisPlanningTool().run()

EDATool().run()

EDAVisualizationTool().run()

result = FeatureEngineeringTool().run()

print(result)

print("\n" + "=" * 60)
print("FEATURE ENGINEERING")
print("=" * 60)

context = ProjectContextManager.get_context()

feature_result = context.feature_engineering_result

print("\nFeature Matrix Shape:")
print(feature_result.features.shape)

print("\nTarget Shape:")
print(feature_result.target.shape)

print("\nFeature Names:")

for feature in feature_result.feature_names:
    print(f"- {feature}")

print("\nFirst Five Rows:")

print(feature_result.features.head())

print("\nEncoded Target:")

print(feature_result.target.head())