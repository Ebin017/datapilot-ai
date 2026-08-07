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
from crew.tools.model_training_tool import (
    ModelTrainingTool,
)
from crew.tools.model_evaluation_tool import (
    ModelEvaluationTool,
)
from crew.tools.explainability_tool import (
    ExplainabilityTool,
)


# --------------------------------------------------
# Run complete pipeline
# --------------------------------------------------

DatasetTool().run(
    dataset_path="datasets/employee_attrition.csv",
)

MetadataTool().run(
    file_name="employee_attrition.csv",
)

DataQualityTool().run()

CleaningStrategyTool().run()

DataCleaningTool().run()

DatasetUnderstandingTool().run()

TargetIdentificationTool().run()

AnalysisPlanningTool().run()

EDATool().run()

EDAVisualizationTool().run()

FeatureEngineeringTool().run()

ModelTrainingTool().run()

ModelEvaluationTool().run()

result = ExplainabilityTool().run()

print(result)

# --------------------------------------------------
# Display results
# --------------------------------------------------

print("\n" + "=" * 60)
print("EXPLAINABILITY")
print("=" * 60)

context = ProjectContextManager.get_context()

explainability = context.explainability_result

print("\nTop Features:\n")

for feature in explainability.top_features:
    print(
        f"{feature}: "
        f"{explainability.feature_importance[feature]:.4f}"
    )

print("\nExpected Value:")
print(explainability.expected_value)

print(
    f"\nTotal SHAP Samples: "
    f"{len(explainability.shap_values)}"
)

if explainability.shap_values:

    print(
        f"SHAP Values Per Sample: "
        f"{len(explainability.shap_values[0])}"
    )