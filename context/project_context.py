from dataclasses import dataclass

import pandas as pd

from models.dataset_info import DatasetInfo


@dataclass
class ProjectContext:
    """
    Shared state for the entire data science workflow.
    """

    dataframe: pd.DataFrame
    dataset_info: DatasetInfo