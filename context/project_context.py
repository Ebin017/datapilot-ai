from dataclasses import dataclass

import pandas as pd

from models.analysis_plan import AnalysisPlan
from models.data_quality_result import DataQualityResult
from models.dataset_info import DatasetInfo
from models.dataset_understanding import DatasetUnderstanding
from models.target_suggestion import TargetSuggestion
from models.eda_result import EDAResult
from models import FeatureEngineeringResult
from models import ModelTrainingResult
from models import ModelEvaluationResult
from models import ExplainabilityResult
from models import BusinessInsightResult
from models.data_cleaning_result import DataCleaningResult
from models.eda_visualization import EDAVisualizationResult
from models.cleaning_plan import CleaningPlan



@dataclass
class ProjectContext:
    """
    Shared state for the entire data science workflow.
    """

    dataframe: pd.DataFrame

    dataset_info: DatasetInfo | None = None

    data_quality: DataQualityResult | None = None

    dataset_understanding: DatasetUnderstanding | None = None

    target_suggestion: TargetSuggestion | None = None

    analysis_plan: AnalysisPlan | None = None

    eda_result: EDAResult | None = None

    feature_engineering_result: FeatureEngineeringResult | None = None

    model_training_result: ModelTrainingResult | None = None

    model_evaluation_result: ModelEvaluationResult | None = None

    explainability_result: ExplainabilityResult | None = None

    business_insight_result: BusinessInsightResult | None = None

    cleaning_plan: CleaningPlan | None = None

    data_cleaning_result: DataCleaningResult | None = None

    eda_visualization_result: EDAVisualizationResult | None = None

    