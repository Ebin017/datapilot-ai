from crewai import Crew

from crew.agents.data_science_planning_agent import (
    create_data_science_planning_agent,
)

from crew.tasks.dataset_understanding_task import (
    create_dataset_understanding_task,
)

from crew.tasks.target_identification_task import (
    create_target_identification_task,
)

from crew.tasks.analysis_planning_task import (
    create_analysis_planning_task,
)


def create_data_science_planning_crew() -> Crew:

    agent = create_data_science_planning_agent()

    understanding_task = (
        create_dataset_understanding_task(
            agent,
        )
    )

    target_task = (
        create_target_identification_task(
            agent,
        )
    )

    planning_task = (
        create_analysis_planning_task(
            agent,
        )
    )

    return Crew(
        agents=[agent],

        tasks=[
            understanding_task,
            target_task,
            planning_task,
        ],

        verbose=True,
    )