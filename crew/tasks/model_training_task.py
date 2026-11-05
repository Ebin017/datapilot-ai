from crewai import Task

from crew.tools.model_training_tool import (
    ModelTrainingTool,
)


def create_model_training_task(agent) -> Task:

    return Task(
        description=(
            "Train the candidate machine learning models using "
            "the processed features and target stored in the shared "
            "ProjectContext.\n\n"

            "The FeatureEngineeringResult and AnalysisPlan must "
            "already exist in ProjectContext before this task runs.\n\n"

            "Use the Model Training Tool to:\n"
            "- Split the processed data into training and test sets "
            "according to the AnalysisPlan\n"
            "- Train all supported candidate models\n"
            "- Evaluate each model using the evaluation metric "
            "specified in the AnalysisPlan\n"
            "- Select the best-performing model\n"
            "- Store all trained models, scores, train/test data, "
            "and the best model in ModelTrainingResult\n\n"

            "Do not load the dataset again.\n"
            "Do not perform feature engineering again.\n"
            "Do not provide arguments to the Model Training Tool.\n\n"

            "The tool reads the AnalysisPlan and "
            "FeatureEngineeringResult directly from the shared "
            "ProjectContext."
        ),

        expected_output=(
            "A concise confirmation containing the number of models "
            "trained, the best model name, and the best model score."
        ),

        agent=agent,

        tools=[
            ModelTrainingTool(),
        ],
    )