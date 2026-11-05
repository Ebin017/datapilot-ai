from crewai import Crew, Process

from crew.context.project_context_manager import ProjectContextManager

from crew.agents.data_preparation_agent import (
    create_data_preparation_agent,
)
from crew.agents.data_science_planning_agent import (
    create_data_science_planning_agent,
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
from crew.tasks.dataset_understanding_task import (
    create_dataset_understanding_task,
)
from crew.tasks.target_identification_task import (
    create_target_identification_task,
)
from crew.tasks.analysis_planning_task import (
    create_analysis_planning_task,
)

from crew.tools.feature_engineering_tool import (
    FeatureEngineeringTool,
)
from crew.tools.model_training_tool import (
    ModelTrainingTool,
)


def create_test_crew():

    # Create agents
    preparation_agent = create_data_preparation_agent()
    planning_agent = create_data_science_planning_agent()

    # Create preparation tasks
    dataset_initialization_task = (
        create_dataset_initialization_task(preparation_agent)
    )

    data_quality_task = create_data_quality_task(preparation_agent)

    cleaning_strategy_task = (
        create_cleaning_strategy_task(preparation_agent)
    )

    data_cleaning_task = (
        create_data_cleaning_task(preparation_agent)
    )

    # Create planning tasks
    dataset_understanding_task = (
        create_dataset_understanding_task(planning_agent)
    )

    target_identification_task = (
        create_target_identification_task(planning_agent)
    )

    analysis_planning_task = (
        create_analysis_planning_task(planning_agent)
    )

    # Create Crew
    crew = Crew(
        agents=[
            preparation_agent,
            planning_agent,
        ],
        tasks=[
            dataset_initialization_task,
            data_quality_task,
            cleaning_strategy_task,
            data_cleaning_task,
            dataset_understanding_task,
            target_identification_task,
            analysis_planning_task,
        ],
        process=Process.sequential,
        verbose=True,
    )

    return crew


if __name__ == "__main__":

    # STEP 1: Run data preparation and planning
    print("\n" + "=" * 50)
    print("DATA PREPARATION AND PLANNING")
    print("=" * 50)

    crew = create_test_crew()

    crew.kickoff(
        inputs={
            "dataset_path": "datasets/employee_salary.csv",
        }
    )

    # STEP 2: Feature Engineering
    print("\n" + "=" * 50)
    print("FEATURE ENGINEERING")
    print("=" * 50)

    context = ProjectContextManager.get_context()

    print("\n--- ANALYSIS PLAN DEBUG ---")
    print("Problem Type:", context.analysis_plan.problem_type)
    print("Numerical Features:", context.analysis_plan.numerical_features)
    print("Categorical Features:", context.analysis_plan.categorical_features)
    print("Feature Encoding:", context.analysis_plan.feature_encoding)
    print("Target Encoding:", context.analysis_plan.target_encoding)

    feature_result = FeatureEngineeringTool().run()

    print(feature_result)

    # STEP 3: Model Training
    print("\n" + "=" * 50)
    print("MODEL TRAINING")
    print("=" * 50)

    training_output = ModelTrainingTool().run()

    print(training_output)

    # Retrieve the actual training result from ProjectContext
    context = ProjectContextManager.get_context()
    training_result = context.model_training_result

    print("\nIndividual Model Scores:")

    for model_name, score in training_result.evaluation_scores.items():
        print(f"{model_name}: {score:.4f}")

    print("\nEvaluation Metric:", training_result.evaluation_metric.upper())
    print("Best Model:", training_result.best_model_name)
    print("Best Score:", round(training_result.best_score, 4))