from clients.llm.gemini_client import GeminiClient
from context.project_context import ProjectContext
from models.dataset_understanding import DatasetUnderstanding
from models.enums.problem_type import ProblemType
from prompts.templates.dataset_understanding_prompt import (
    build_dataset_understanding_prompt,
)
from pydantic import ValidationError


class DatasetUnderstandingService:
    """
    Creates a high-level understanding of a dataset using Gemini.
    """

    def __init__(self):
        self.gemini_client = GeminiClient()

    def understand(
        self,
        context: ProjectContext,
    ) -> DatasetUnderstanding:

        prompt = build_dataset_understanding_prompt(context)

        response = self.gemini_client.generate(prompt)

        try:
            return DatasetUnderstanding.model_validate_json(response)

        except ValidationError as e:
            raise ValueError(
                "Failed to parse Gemini response."
            ) from e
        


#     def _build_prompt(
#         self,
#         context: ProjectContext,
#     ) -> str:
#         """
#         Build a prompt describing the dataset.
#         """

#         dataset_info = context.dataset_info
#         data_quality = context.data_quality

#         total_missing = sum(data_quality.missing_values.values())

#         prompt = f"""
# You are an experienced Data Scientist.

# Analyze the following dataset metadata.

# Dataset Information

# File Name:
# {dataset_info.file_name}

# Rows:
# {dataset_info.rows}

# Columns:
# {dataset_info.columns}

# Numeric Columns:
# {", ".join(dataset_info.numeric_columns)}

# Categorical Columns:
# {", ".join(dataset_info.categorical_columns)}

# Data Types:
# {dataset_info.data_types}

# Data Quality

# Missing Values:
# {total_missing}

# Duplicate Rows:
# {data_quality.duplicate_rows}

# Your task:

# 1. Write a short summary of the dataset.
# 2. List 4 important observations.
# 3. Suggest whether this is likely a classification or regression problem.
# 4. Explain your reasoning.

# Keep the response concise.
# """

#         return prompt.strip()