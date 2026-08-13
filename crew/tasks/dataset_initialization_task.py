from crewai import Task

from crew.tools.dataset_tool import DatasetTool


def create_dataset_initialization_task(agent) -> Task:

    return Task(
        description=(
            "Load the dataset provided at {dataset_path} "
            "using the Dataset Loader tool. "
            "This must be completed first because all "
            "subsequent data preparation tools depend on "
            "the shared ProjectContext created by the "
            "dataset loader."
        ),

        expected_output=(
            "The dataset is successfully loaded and the "
            "shared ProjectContext has been initialized."
        ),

        agent=agent,

        tools=[
            DatasetTool(),
        ],
    )