from crew.context.project_context_manager import (
    ProjectContextManager,
)

from crew.tools.dataset_tool import DatasetTool
from crew.tools.metadata_tool import MetadataTool
from crew.tools.data_quality_tool import DataQualityTool
from crew.tools.cleaning_strategy_tool import CleaningStrategyTool
from crew.tools.data_cleaning_tool import DataCleaningTool
from crew.tools.dataset_understanding_tool import DatasetUnderstandingTool
from crew.tools.target_identification_tool import TargetIdentificationTool
from crew.tools.analysis_planning_tool import AnalysisPlanningTool
from crew.tools.eda_tool import EDATool
from crew.tools.eda_visualization_tool import EDAVisualizationTool
from crew.tools.feature_engineering_tool import FeatureEngineeringTool
from crew.tools.model_training_tool import ModelTrainingTool
from crew.tools.model_evaluation_tool import ModelEvaluationTool
from crew.tools.explainability_tool import ExplainabilityTool
from crew.tools.business_insight_tool import BusinessInsightTool


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

ExplainabilityTool().run()

result = BusinessInsightTool().run()

print(result)

print("\n" + "=" * 60)
print("BUSINESS INSIGHTS")
print("=" * 60)

context = ProjectContextManager.get_context()

insights = context.business_insight_result

print("\nExecutive Summary:\n")
print(insights.executive_summary)

print("\nKey Findings:")
for finding in insights.key_findings:
    print(f"- {finding}")

print("\nModel Performance Summary:\n")
print(insights.model_performance_summary)

print("\nFeature Importance Summary:\n")
print(insights.feature_importance_summary)

print("\nBusiness Recommendations:")
for recommendation in insights.business_recommendations:
    print(f"- {recommendation}")

print("\nRisks and Limitations:")
for risk in insights.risks_and_limitations:
    print(f"- {risk}")

print("\nNext Steps:")
for step in insights.next_steps:
    print(f"- {step}")