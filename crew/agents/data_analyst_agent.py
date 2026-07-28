from crewai import Agent

from config.settings import Settings


def create_data_analyst_agent() -> Agent:
    return Agent(
        role="Senior Data Analyst",
        goal=(
            "Analyze datasets, understand their structure, "
            "perform exploratory data analysis, identify data "
            "quality issues, and prepare the dataset for machine "
            "learning."
        ),
        backstory=(
            "You are an experienced data analyst with expertise "
            "in statistics, exploratory data analysis, and data "
            "preprocessing. You work as part of an AI Data Science "
            "Team and collaborate with other specialists."
        ),
        llm=Settings.LLM_MODEL,
        verbose=True,
    )