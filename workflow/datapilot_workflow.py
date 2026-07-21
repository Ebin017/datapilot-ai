from pathlib import Path

from context.project_context import ProjectContext

from services.dataset.dataset_service import DatasetService
from services.dataset.metadata_service import MetadataService
from services.dataset.data_quality_service import DataQualityService

from services.understanding.dataset_understanding_service import (
    DatasetUnderstandingService,
)
from services.understanding.ai_target_identification_service import (
    AITargetIdentificationService,
)

from services.planning.ai_analysis_planner import AIAnalysisPlanner

from services.execution.eda.exploratory_data_analysis_service import ExploratoryDataAnalysisService

from services.execution.feature_engineering.feature_engineering_service import (
    FeatureEngineeringService,
)

from services.training.model_training_service import (
    ModelTrainingService,
)

from services.evaluation.model_evaluation_service import ModelEvaluationService

from services.explainability.explainability_service import ExplainabilityService
class DataPilotWorkflow:
    """
    Coordinates the complete data science workflow.
    """

    def __init__(self):

        self.dataset_service = DatasetService()

        self.metadata_service = MetadataService()

        self.data_quality_service = DataQualityService()

        self.understanding_service = DatasetUnderstandingService()

        self.target_service = AITargetIdentificationService()

        self.analysis_planner = AIAnalysisPlanner()

        self.eda_service = ExploratoryDataAnalysisService()

        self.feature_engineering_service = FeatureEngineeringService()

        self.model_training_service = ModelTrainingService()

        self.model_evaluation_service = ModelEvaluationService()

        self.explainability_service = ExplainabilityService()

    def run(
        self,
        dataset_path: Path,
    ) -> ProjectContext:

        # Load dataset
        dataframe = self.dataset_service.load_dataset(
            dataset_path,
        )

        # Metadata
        dataset_info = self.metadata_service.extract(
            dataframe=dataframe,
            file_name=dataset_path.name,
        )

        # Data quality
        data_quality = self.data_quality_service.analyze(
            dataframe,
        )

        # Shared context
        context = ProjectContext(
            dataframe=dataframe,
            dataset_info=dataset_info,
            data_quality=data_quality,
        )

        # Dataset understanding
        context.dataset_understanding = (
            self.understanding_service.understand(
                context,
            )
        )

        # Target suggestion
        context.target_suggestion = (
            self.target_service.identify(
                context,
            )
        )

        # Analysis plan
        context.analysis_plan = (
            self.analysis_planner.create_plan(
                context,
            )
        )

        # eda
        context.eda_result = self.eda_service.analyze(context)

        # feature engineering
        context.feature_engineering_result = (
            self.feature_engineering_service.transform(
                context,
            )
        )

        # training
        context.model_training_result = (
            self.model_training_service.train(
                context,
            )
        )

        # evaluation
        context.model_evaluation_result = (
            self.model_evaluation_service.evaluate(
                context,
            )
        )

        # explainabiliy
        context.explainability_result = (
            self.explainability_service.explain(
                context,
            )
        )

        
        return context