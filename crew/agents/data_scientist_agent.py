from crewai import Agent

from config.settings import Settings


def create_data_scientist_agent() -> Agent:
    """
    Creates the Data Scientist agent.
    """

    return Agent(
        role="Senior Data Scientist",

        goal=(
            "Analyze datasets, identify machine learning problems, "
            "and recommend the best analysis strategy."
        ),

        backstory=(
            "You are an experienced Senior Data Scientist with expertise "
            "in machine learning, statistics, feature engineering, "
            "and exploratory data analysis."
        ),

        verbose=True,

        llm=f"gemini/{Settings.GEMINI_MODEL}",
    )