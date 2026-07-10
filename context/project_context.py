from dataclasses import dataclass

import pandas as pd

from models.analysis_plan import AnalysisPlan
from models.data_quality_result import DataQualityResult
from models.dataset_info import DatasetInfo
from models.dataset_understanding import DatasetUnderstanding
from models.target_suggestion import TargetSuggestion


@dataclass
class ProjectContext:
    """
    Shared state for the entire data science workflow.
    """

    dataframe: pd.DataFrame

    dataset_info: DatasetInfo

    data_quality: DataQualityResult

    dataset_understanding: DatasetUnderstanding | None = None

    target_suggestion: TargetSuggestion | None = None

    analysis_plan: AnalysisPlan | None = None