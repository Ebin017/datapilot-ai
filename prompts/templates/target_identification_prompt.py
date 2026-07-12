from context.project_context import ProjectContext


def build_target_identification_prompt(
    context: ProjectContext,
) -> str:
    """
    Build the prompt for identifying the prediction target.
    """

    dataset_info = context.dataset_info
    data_quality = context.data_quality

    total_missing = sum(
        data_quality.missing_values.values()
    )

    return f"""
You are an experienced Data Scientist.

Your task is to identify the most likely prediction target.

Dataset Information

File Name:
{dataset_info.file_name}

Rows:
{dataset_info.rows}

Columns:
{dataset_info.columns}

Column Names:
{dataset_info.column_names}

Numeric Columns:
{", ".join(dataset_info.numeric_columns)}

Categorical Columns:
{", ".join(dataset_info.categorical_columns)}

Data Types:
{dataset_info.data_types}

Missing Values:
{total_missing}

Duplicate Rows:
{data_quality.duplicate_rows}

Return ONLY valid JSON.

Do not include markdown.

Do not include explanations.

Return exactly this schema:

{{
    "column_name": "string",
    "problem_type": "classification or regression",
    "confidence": 0.95,
    "reason": "string"
}}
""".strip()