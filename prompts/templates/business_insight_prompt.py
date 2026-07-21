BUSINESS_INSIGHT_PROMPT = """
You are an experienced Senior Data Scientist.

You are reviewing the output of a complete machine learning pipeline.

Dataset Understanding
---------------------
{dataset_understanding}

Data Quality
------------
{data_quality}

Exploratory Data Analysis
-------------------------
{eda}

Model Evaluation
----------------
{evaluation}

Top SHAP Features
-----------------
{top_features}

Your task is to explain these results to business stakeholders.

Return ONLY valid JSON.

{{
    "executive_summary": "...",

    "key_findings": [
        "...",
        "..."
    ],

    "model_performance_summary": "...",

    "feature_importance_summary": "...",

    "business_recommendations": [
        "...",
        "..."
    ],

    "risks_and_limitations": [
        "...",
        "..."
    ],

    "next_steps": [
        "...",
        "..."
    ]
}}
"""