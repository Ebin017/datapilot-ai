from pathlib import Path

from crewai.tools import BaseTool
from pydantic import Field

from context.project_context import ProjectContext
from crew.context.project_context_manager import (
    ProjectContextManager,
)
from services.dataset.dataset_service import DatasetService


class DatasetTool(BaseTool):
    """
    Loads a dataset and initializes the shared ProjectContext.
    """

    name: str = "Dataset Loader"

    description: str = (
        "Load a dataset from a CSV or Excel file and initialize "
        "the project context."
    )

    dataset_service: DatasetService = Field(
        default_factory=DatasetService,
    )

    def _run(
        self,
        dataset_path: str,
    ) -> str:

        # Load dataset
        dataframe = self.dataset_service.load_dataset(
            Path(dataset_path),
        )

        # Initialize ProjectContext
        context = ProjectContext(
            dataframe=dataframe,
        )

        # Store ProjectContext
        ProjectContextManager.set_context(
            context,
        )

        return (
            "Dataset loaded successfully.\n"
            f"Rows: {len(dataframe)}\n"
            f"Columns: {len(dataframe.columns)}\n"
            f"Column Names: {', '.join(dataframe.columns)}"
        )