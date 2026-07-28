from crew.crews.datapilot_crew import (
    create_datapilot_crew,
)

crew = create_datapilot_crew()

result = crew.kickoff(
    inputs={
        "dataset_path": "datasets/employee_attrition.csv",
    }
)

print(result)