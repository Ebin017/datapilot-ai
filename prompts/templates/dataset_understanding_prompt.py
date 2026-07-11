from context.project_context import ProjectContext


def build_dataset_understanding_prompt(
    context: ProjectContext,
) -> str:
    """
    Build the prompt for understanding a dataset.
    """

    dataset_info = context.dataset_info
    data_quality = context.data_quality

    total_missing = sum(
        data_quality.missing_values.values()
    )

    return f"""
You are an experienced Data Scientist.

Analyze the dataset metadata below.

Dataset Information

File Name:
{dataset_info.file_name}

Rows:
{dataset_info.rows}

Columns:
{dataset_info.columns}

Numeric Columns:
{", ".join(dataset_info.numeric_columns)}

Categorical Columns:
{", ".join(dataset_info.categorical_columns)}

Data Types:
{dataset_info.data_types}

Data Quality

Missing Values:
{total_missing}

Duplicate Rows:
{data_quality.duplicate_rows}

Return ONLY valid JSON.

Do not include markdown.

Do not include code fences.

Do not include explanations.

The JSON must exactly match this schema:

{{
    "summary": "string",
    "likely_problem_type": "classification or regression",
    "observations": [
        "string",
        "string",
        "string"
    ]
}}
""".strip()