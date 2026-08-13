from crewai import Agent, LLM

from config.settings import Settings


def create_data_preparation_agent() -> Agent:

    llm = LLM(
        model=f"ollama/{Settings.OLLAMA_MODEL}",
        base_url="http://localhost:11434",
    )

    return Agent(
        role="Senior Data Preparation Specialist",

        goal=(
            "Load datasets, inspect their metadata and quality, "
            "identify data quality problems, and prepare clean "
            "datasets for downstream machine learning analysis."
        ),

        backstory=(
            "You are an experienced data preparation specialist "
            "with expertise in dataset ingestion, metadata analysis, "
            "data quality assessment, and data cleaning. You ensure "
            "that datasets are reliable and ready for machine "
            "learning workflows."
        ),

        llm=llm,

        verbose=True,
    )