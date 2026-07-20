from pathlib import Path

from workflow.datapilot_workflow import DataPilotWorkflow


def main():

    workflow = DataPilotWorkflow()

    context = workflow.run(
        Path("data/employee_attrition.csv"),
    )

    print("\nDataset Information")
    print("-" * 40)
    print(context.dataset_info)

    print("\nFirst Five Rows")
    print("-" * 40)
    print(context.dataframe.head())

    print("\nData Quality")
    print("-" * 40)
    print(context.data_quality)

    print("\nDataset Understanding")
    print("-" * 40)
    print(context.dataset_understanding)

    print("\nTarget Suggestion")
    print("-" * 40)
    print(context.target_suggestion)

    print("\nAnalysis Plan")
    print("-" * 40)
    print(context.analysis_plan)

    print("\nEDA")
    print("-" * 40)
    print(context.eda_result)

    print("\nFeature Engineering")
    print("-" * 40)

    print("Features")
    print(context.feature_engineering_result.features)

    print("\nTarget")
    print(context.feature_engineering_result.target)

    print("\nFeature Names")
    print(context.feature_engineering_result.feature_names)

    print("\nModel Training")
    print("-" * 40)
    print(context.model_training_result)


if __name__ == "__main__":
    main()