from crewai import Task

from crew.tools.metadata_tool import MetadataTool
from crew.tools.data_quality_tool import DataQualityTool


def create_data_quality_task(agent) -> Task:

    return Task(
        description=(
            "Analyze the dataset that has already been loaded "
            "into the shared ProjectContext.\n\n"

            "STEP 1: METADATA EXTRACTION\n"
            "Use the Metadata Extractor tool first.\n"
            "This tool takes NO arguments. It automatically retrieves "
            "the DataFrame and filename from ProjectContext.\n\n"

            "STEP 2: DATA QUALITY ANALYSIS\n"
            "After metadata extraction, use the Data Quality Analyzer "
            "tool.\n"
            "This tool also takes NO arguments. It automatically "
            "retrieves the DataFrame from ProjectContext.\n\n"

            "IMPORTANT RULES:\n"
            "- Do not pass arguments to either tool.\n"
            "- Do not load the dataset again.\n"
            "- Do not manually analyze the dataset.\n"
            "- Do not write or suggest pandas code.\n"
            "- Do not invent analysis results.\n"
            "- If either tool fails, clearly report the failure.\n"
            "- Only report results returned by the tools."
        ),

        expected_output=(
            "Dataset metadata has been extracted and data quality "
            "analysis has been completed successfully. Both results "
            "are stored in the shared ProjectContext."
        ),

        agent=agent,

        tools=[
            MetadataTool(),
            DataQualityTool(),
        ],
    )