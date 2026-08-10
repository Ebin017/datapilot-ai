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
from crew.tools.business_insight_tool import (
    BusinessInsightTool,
)
from crew.tools.report_tool import ReportTool


# ==================================================
# Run complete pipeline
# ==================================================

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

BusinessInsightTool().run()


# ==================================================
# Generate final report
# ==================================================

result = ReportTool().run()


# ==================================================
# Display result
# ==================================================

print(
    "\n" + "=" * 60
)

print(
    "REPORT GENERATION"
)

print(
    "=" * 60
)

print()

print(result)


# ==================================================
# Verify ProjectContext
# ==================================================

context = ProjectContextManager.get_context()

if context.report_result:

    print(
        "\nReport Title:"
    )

    print(
        context.report_result.report_title
    )

    print(
        "\nReport Path:"
    )

    print(
        context.report_result.report_path
    )