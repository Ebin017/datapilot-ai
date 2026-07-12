from context.project_context import ProjectContext


def build_analysis_planning_prompt(
    context: ProjectContext,
) -> str:
    """
    Build the prompt for creating an analysis plan.
    """

    understanding = context.dataset_understanding
    target = context.target_suggestion
    dataset_info = context.dataset_info

    return f"""
You are an experienced Senior Data Scientist.

Create a machine learning analysis plan.

Dataset Summary

{understanding.summary}

Problem Type

{understanding.likely_problem_type.value}

Target Column

{target.column_name}

Dataset Information

Rows:
{dataset_info.rows}

Columns:
{dataset_info.columns}

Numeric Columns:
{", ".join(dataset_info.numeric_columns)}

Categorical Columns:
{", ".join(dataset_info.categorical_columns)}

Return ONLY valid JSON.

Do not include markdown.

Do not include explanations.

Return a machine-executable plan. Do not describe the steps in natural language.

Do not omit any field, even if its value is null.

Return exactly this schema:

{{
    "target_column": "string",
    "problem_type": "classification or regression",
    "evaluation_metric": "string",
    "train_test_split": 0.2,
    "random_state": 42,
    "stratify_split": true,
    "columns_to_drop": [
        "CustomerID"
    ],
    "numerical_features": [
        "Age",
        "Income"
    ],
    "categorical_features": [],
    "scaling_method": "standard",
    "feature_encoding": null,
    "target_encoding": "label"
}}

""".strip()