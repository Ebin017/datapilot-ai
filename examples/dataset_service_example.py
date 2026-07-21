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

    print()

    print("Model Evaluation")
    print("-" * 40)

    print(
        context.model_evaluation_result,
    )

    print("\nExplainability")
    print("-" * 40)

    for feature, score in (
        context.explainability_result
        .feature_importance
        .items()
    ):
        print(f"{feature}: {score:.4f}")
    
    result = context.business_insight_result

    print("\nAI Business Insights")
    print("-" * 40)

    print("\nExecutive Summary")
    print(result.executive_summary)

    print("\nKey Findings")
    for finding in result.key_findings:
        print(f"• {finding}")

    print("\nModel Performance")
    print(result.model_performance_summary)

    print("\nFeature Importance")
    print(result.feature_importance_summary)

    print("\nBusiness Recommendations")
    for recommendation in result.business_recommendations:
        print(f"• {recommendation}")

    print("\nRisks & Limitations")
    for risk in result.risks_and_limitations:
        print(f"• {risk}")

    print("\nNext Steps")
    for step in result.next_steps:
        print(f"• {step}")


if __name__ == "__main__":
    main()
