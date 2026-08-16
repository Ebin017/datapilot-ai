from crewai import Agent, LLM

from config.settings import Settings


def create_data_science_planning_agent() -> Agent:

    llm = LLM(
        model=f"ollama/{Settings.OLLAMA_MODEL}",
        base_url="http://localhost:11434",
    )

    return Agent(
        role="Senior Data Science Planning Specialist",

        goal=(
            "Understand the prepared dataset, identify the most "
            "appropriate prediction target and machine learning "
            "problem type, and create a reliable analysis plan "
            "for downstream machine learning."
        ),

        backstory=(
            "You are an experienced data scientist specializing "
            "in dataset understanding, target identification, "
            "machine learning problem formulation, feature "
            "analysis, preprocessing decisions, evaluation "
            "metrics, and model selection. You carefully inspect "
            "the available dataset information before making "
            "modeling decisions."
        ),

        llm=llm,

        verbose=True,
    )