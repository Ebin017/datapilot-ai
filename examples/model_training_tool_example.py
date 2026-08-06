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

result = ModelTrainingTool().run()

print(result)

print("\n" + "=" * 60)
print("MODEL TRAINING")
print("=" * 60)

context = ProjectContextManager.get_context()

training = context.model_training_result

print("\nEvaluation Scores:")

for model, score in training.evaluation_scores.items():
    print(f"{model}: {score:.4f}")

print(f"\nBest Model:")
print(training.best_model_name)

print(f"\nBest Score:")
print(training.best_score)

print("\nTrain Shape:")
print(training.x_train.shape)

print("\nTest Shape:")
print(training.x_test.shape)