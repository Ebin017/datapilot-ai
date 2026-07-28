from crewai import Crew

from crew.agents.data_analyst_agent import (
    create_data_analyst_agent,
)

from crew.tasks.analyze_dataset_task import (
    create_analysis_task,
)


def create_datapilot_crew():

    analyst = create_data_analyst_agent()

    task = create_analysis_task(
        analyst,
    )

    return Crew(
        agents=[analyst],
        tasks=[task],
        verbose=True,
    )