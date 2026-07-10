from pathlib import Path

from workflow.datapilot_workflow import DataPilotWorkflow


def main():

    workflow = DataPilotWorkflow()

    context = workflow.run(
        Path("data/customer_churn.csv"),
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


if __name__ == "__main__":
    main()