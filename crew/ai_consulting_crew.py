from crewai import Crew
from crewai import Process

from crew.agents.data_scientist_agent import (
    create_data_scientist_agent,
)

from crew.tasks.dataset_understanding_task import (
    create_dataset_understanding_task,
)


class AIConsultingCrew:
    """
    Crew responsible for AI consulting tasks.
    """

    def understand_dataset(
        self,
        prompt: str,
    ) -> str:

        agent = create_data_scientist_agent()

        task = create_dataset_understanding_task(
            agent,
            prompt,
        )

        crew = Crew(
            agents=[agent],

            tasks=[task],

            process=Process.sequential,

            verbose=True,
        )

        result = crew.kickoff()

        return str(result)