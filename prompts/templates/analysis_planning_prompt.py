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

Feature Engineering Rules

1. Use the Numeric Columns and Categorical Columns provided above.

2. Exclude the target column from both numerical_features and categorical_features.

3. Exclude identifier columns (such as CustomerID, EmployeeID, ID, RecordID, etc.) from both feature lists.
   Include these identifier columns in columns_to_drop.

4. If one or more categorical feature columns remain after removing the target and identifier columns:
   - feature_encoding must be "one_hot"
   - categorical_features must contain ALL remaining categorical feature columns

5. If no categorical feature columns remain:
   - feature_encoding must be null
   - categorical_features must be an empty list

6. If one or more numerical feature columns remain after removing identifier columns:
   - numerical_features must contain ALL remaining numerical feature columns

7. If the target column is categorical:
   - target_encoding must be "label"

8. Use standard scaling for numerical features unless there is a strong reason not to.

Return ONLY valid JSON.

Do not include markdown.

Do not include explanations.

Return a machine-executable plan.

Do not omit any field, even if its value is null.

Recommend 2-3 candidate models appropriate for the dataset.
Do not recommend deep learning models unless the dataset characteristics justify them.

Double-check before returning:
- Every categorical feature column is included.
- Every numerical feature column is included.
- The target column is excluded.
- Identifier columns are excluded from feature lists and added to columns_to_drop.

Return exactly this schema:

{{
  "target_column": "Attrition",
  "problem_type": "classification",
  "evaluation_metric": "f1_score",
  "train_test_split": 0.2,
  "random_state": 42,
  "stratify_split": true,
  "columns_to_drop": [
    "EmployeeID"
  ],
  "numerical_features": [
    "Age",
    "Salary",
    "YearsAtCompany"
  ],
  "categorical_features": [
    "Gender",
    "Department",
    "Education",
    "WorkLifeBalance",
    "OverTime",
    "MaritalStatus"
  ],
  "scaling_method": "standard",
  "feature_encoding": "one_hot",
  "target_encoding": "label",
  "candidate_models": [
    {{
      "name": "logistic_regression",
      "reason": "Good baseline for binary classification."
    }},
    {{
      "name": "random_forest",
      "reason": "Handles nonlinear relationships."
    }},
    {{
      "name": "xgboost",
      "reason": "Strong performer on tabular datasets."
    }}
  ]
}}
""".strip()