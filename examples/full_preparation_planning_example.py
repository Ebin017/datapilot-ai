from crew.crews.data_preparation_crew import (
    create_data_preparation_crew,
)

from crew.crews.data_science_planning_crew import (
    create_data_science_planning_crew,
)


if __name__ == "__main__":

    preparation_crew = (
        create_data_preparation_crew()
    )

    preparation_result = preparation_crew.kickoff(
        inputs={
            "dataset_path": (
                "datasets/employee_attrition.csv"
            ),
        }
    )

    print("\n")
    print("=" * 60)
    print("DATA PREPARATION COMPLETED")
    print("=" * 60)
    print(preparation_result)

    planning_crew = (
        create_data_science_planning_crew()
    )

    planning_result = planning_crew.kickoff()

    print("\n")
    print("=" * 60)
    print("DATA SCIENCE PLANNING COMPLETED")
    print("=" * 60)
    print(planning_result)