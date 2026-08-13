from crewai import Task

from crew.tools.metadata_tool import MetadataTool
from crew.tools.data_quality_tool import DataQualityTool


def create_data_quality_task(agent) -> Task:

    return Task(
        description=(
            "Analyze the dataset that has already been loaded "
            "into the shared ProjectContext.\n\n"

            "First extract the dataset metadata using the "
            "Metadata Extractor tool.\n\n"

            "Then analyze the dataset for data quality issues "
            "using the Data Quality Analyzer tool.\n\n"

            "Do not attempt to load the dataset again."
        ),

        expected_output=(
            "The shared ProjectContext contains the dataset "
            "metadata and completed data quality assessment."
        ),

        agent=agent,

        tools=[
            MetadataTool(),
            DataQualityTool(),
        ],
    )