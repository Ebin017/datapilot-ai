from crewai import Crew

from crew.agents.data_preparation_agent import (
    create_data_preparation_agent,
)

from crew.tasks.dataset_initialization_task import (
    create_dataset_initialization_task,
)

from crew.tasks.data_quality_task import (
    create_data_quality_task,
)

from crew.tasks.cleaning_strategy_task import (
    create_cleaning_strategy_task,
)

from crew.tasks.data_cleaning_task import (
    create_data_cleaning_task,
)


def create_test_crew():

    agent = create_data_preparation_agent()

    initialization_task = (
        create_dataset_initialization_task(
            agent,
        )
    )

    data_quality_task = (
        create_data_quality_task(
            agent,
        )
    )

    cleaning_strategy_task = (
        create_cleaning_strategy_task(
            agent,
        )
    )

    data_cleaning_task = (
        create_data_cleaning_task(
            agent,
        )
    )

    return Crew(
        agents=[agent],

        tasks=[
            initialization_task,
            data_quality_task,
            cleaning_strategy_task,
            data_cleaning_task,
        ],

        verbose=True,
    )


if __name__ == "__main__":

    crew = create_test_crew()

    result = crew.kickoff(
        inputs={
            "dataset_path": (
                "datasets/cleaning1.csv"
            ),
            "file_name": (
                "cleaning1.csv"
            ),
        }
    )

    print(
        "\n" + "=" * 60
    )

    print(
        "DATA PREPARATION CREW RESULT"
    )

    print(
        "=" * 60
    )

    print(result)