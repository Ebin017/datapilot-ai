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
        "Extract metadata from the dataset already loaded "
        "in the shared ProjectContext. "
        "IMPORTANT: This tool takes NO arguments. "
        "Do not provide file_name or any other parameters. "
        "The tool automatically uses the dataset and filename "
        "stored in ProjectContext."
    )

    metadata_service: MetadataService = Field(
        default_factory=MetadataService,
    )

    def _run(self) -> str:

        context = ProjectContextManager.get_context()

        context.dataset_info = (
            self.metadata_service.extract(
                dataframe=context.dataframe,
                file_name=context.file_name or "unknown",
            )
        )

        return (
            "Dataset metadata extracted successfully.\n"
            f"Rows: {context.dataset_info.rows}\n"
            f"Columns: {context.dataset_info.columns}\n"
            f"File Name: {context.dataset_info.file_name}"
        )