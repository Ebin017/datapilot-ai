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

FeatureEngineeringTool().run()

ModelTrainingTool().run()

result = ModelEvaluationTool().run()

print(result)

print("\n" + "=" * 60)
print("MODEL EVALUATION")
print("=" * 60)

context = ProjectContextManager.get_context()

evaluation = context.model_evaluation_result

print(f"\nAccuracy: {evaluation.accuracy:.4f}")
print(f"Precision: {evaluation.precision:.4f}")
print(f"Recall: {evaluation.recall:.4f}")
print(f"F1 Score: {evaluation.f1_score:.4f}")

print("\nConfusion Matrix:")

for row in evaluation.confusion_matrix:
    print(row)

print("\nClassification Report:")

for label, metrics in evaluation.classification_report.items():

    print(f"\n{label}")

    if isinstance(metrics, dict):

        for metric, value in metrics.items():
            print(f"  {metric}: {value:.4f}")

    else:
        print(metrics)