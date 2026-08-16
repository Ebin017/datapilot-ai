from context.project_context import ProjectContext


def build_analysis_planning_prompt(
    context: ProjectContext,
) -> str:
    """
    Build the prompt for creating a machine learning analysis plan.
    """

    understanding = context.dataset_understanding
    target = context.target_suggestion
    dataset_info = context.dataset_info

    return f"""
You are an experienced Senior Data Scientist.

Create a machine learning analysis plan based ONLY on the
dataset information and analysis results provided below.

Do not invent dataset columns.
Do not copy values from the example schema.
Do not assume the dataset is an employee attrition dataset.

============================================================
DATASET UNDERSTANDING
============================================================

Summary:
{understanding.summary}

Likely Problem Type:
{understanding.likely_problem_type.value}

Observations:
{understanding.observations}

============================================================
TARGET IDENTIFICATION
============================================================

Target Column:
{target.column_name}

Problem Type:
{target.problem_type.value}

Confidence:
{target.confidence}

Reason:
{target.reason}

============================================================
DATASET INFORMATION
============================================================

Rows:
{dataset_info.rows}

Columns:
{dataset_info.columns}

Column Names:
{", ".join(dataset_info.column_names)}

Numeric Columns:
{", ".join(dataset_info.numeric_columns)}

Categorical Columns:
{", ".join(dataset_info.categorical_columns)}

Data Types:
{dataset_info.data_types}

============================================================
FEATURE ENGINEERING RULES
============================================================

1. Use the Numeric Columns and Categorical Columns provided
   above.

2. Exclude the target column from both
   numerical_features and categorical_features.

3. Identify identifier columns such as:
   CustomerID, EmployeeID, ID, RecordID, UserID, TransactionID,
   or other columns that uniquely identify individual records.

4. Identifier columns must:
   - be excluded from numerical_features
   - be excluded from categorical_features
   - be included in columns_to_drop

5. Do not drop normal business features simply because they
   contain categorical values.

6. If one or more categorical feature columns remain:
   - feature_encoding must be "one_hot"
   - categorical_features must contain ALL remaining
     categorical feature columns

7. If no categorical feature columns remain:
   - feature_encoding must be null
   - categorical_features must be an empty list

8. If one or more numerical feature columns remain:
   - numerical_features must contain ALL remaining numerical
     feature columns

9. If no numerical feature columns remain:
   - numerical_features must be an empty list

10. If the target column is categorical:
    - target_encoding must be "label"

11. If the target column is already numerical and appropriate
    for regression:
    - target_encoding must be null

12. Use standard scaling for numerical features unless there
    is a strong reason not to.

13. Choose an evaluation metric appropriate for the identified
    problem type.

14. For classification:
    - consider class balance when selecting the metric
    - use stratified splitting when appropriate

15. For regression:
    - use an appropriate regression metric such as
      RMSE, MAE, or R2

16. Recommend 2-3 candidate models appropriate for the
    identified problem type and dataset characteristics.

17. Do not recommend deep learning models unless the dataset
    characteristics justify their use.

============================================================
TRAIN / TEST SPLIT
============================================================

Use a reasonable train/test split.

The default should be:

- train/test split: 80/20
- random_state: 42

For classification, use stratification when appropriate.

============================================================
IMPORTANT
============================================================

The values in the schema below are examples of the required
FORMAT ONLY.

DO NOT copy example values such as:
- Attrition
- EmployeeID
- Age
- Salary
- Gender
- Department

Generate every value from the actual dataset information
provided above.

Double-check the final plan before returning it.

Verify that:

- target_column exists in the dataset
- target_column is excluded from feature lists
- every valid numerical feature is included
- every valid categorical feature is included
- identifier columns are excluded from feature lists
- identifier columns are included in columns_to_drop
- the problem_type matches the identified target
- the evaluation_metric matches the problem type
- candidate_models match the problem type
- all required fields are present

============================================================
OUTPUT FORMAT
============================================================

Return ONLY valid JSON.

Do not include markdown.

Do not include code fences.

Do not include explanations outside the JSON.

Return exactly this schema:

{{
    "target_column": "string",
    "problem_type": "classification",
    "evaluation_metric": "string",
    "train_test_split": 0.2,
    "random_state": 42,
    "stratify_split": true,
    "columns_to_drop": [
        "string"
    ],
    "numerical_features": [
        "string"
    ],
    "categorical_features": [
        "string"
    ],
    "scaling_method": "standard",
    "feature_encoding": "one_hot",
    "target_encoding": "label",
    "candidate_models": [
        {{
            "name": "string",
            "reason": "string"
        }},
        {{
            "name": "string",
            "reason": "string"
        }}
    ]
}}

Remember:
The schema values are examples only.
Use the actual dataset information to generate the final plan.
""".strip()