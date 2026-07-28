from pathlib import Path

from crewai.tools import BaseTool
from pydantic import Field

from crew.context.project_context_manager import (
    ProjectContextManager,
)
from services.dataset.metadata_service import MetadataService


class MetadataTool(BaseTool):
    """
    Extracts dataset metadata and stores it in ProjectContext.
    """

    name: str = "Metadata Extractor"

    description: str = (
        "Extract metadata from the loaded dataset."
    )

    metadata_service: MetadataService = Field(
        default_factory=MetadataService,
    )

    def _run(
        self,
        file_name: str,
    ) -> str:

        context = ProjectContextManager.get_context()

        context.dataset_info = (
            self.metadata_service.extract(
                dataframe=context.dataframe,
                file_name=Path(file_name).name,
            )
        )

        return (
            "Dataset metadata extracted successfully.\n"
            f"Rows: {context.dataset_info.rows}\n"
            f"Columns: {context.dataset_info.columns}\n"
            f"File Name: {context.dataset_info.file_name}"
        )