from crewai import Task

from crew.tools.metadata_tool import MetadataTool
from crew.tools.data_quality_tool import DataQualityTool
from crew.tools.cleaning_strategy_tool import (
    CleaningStrategyTool,
)
from crew.tools.data_cleaning_tool import (
    DataCleaningTool,
)


def create_data_preparation_task(agent) -> Task:

    return Task(
        description=(
            "Prepare the already-loaded dataset for downstream "
            "machine learning analysis.\n\n"

            "The dataset has already been loaded and the shared "
            "ProjectContext has been initialized by the previous "
            "task.\n\n"

            "Follow this sequence:\n"
            "1. Extract dataset metadata.\n"
            "2. Analyze data quality.\n"
            "3. Generate an appropriate cleaning strategy.\n"
            "4. Execute the cleaning strategy.\n\n"

            "All tools operate on the shared ProjectContext. "
            "Do not attempt to load the dataset again."
        ),

        expected_output=(
            "The shared ProjectContext contains dataset metadata, "
            "data quality results, cleaning strategy, and data "
            "cleaning results. The dataset is ready for downstream "
            "machine learning analysis."
        ),

        agent=agent,

        tools=[
            MetadataTool(),
            DataQualityTool(),
            CleaningStrategyTool(),
            DataCleaningTool(),
        ],
    )

# delete this file