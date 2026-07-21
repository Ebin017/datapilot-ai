import numpy as np
import shap

from context.project_context import ProjectContext
from models import ExplainabilityResult


class ExplainabilityService:
    """
    Generates SHAP-based explainability for the best trained model.
    """

    def explain(
        self,
        context: ProjectContext,
    ) -> ExplainabilityResult:

        training = context.model_training_result

        model = training.trained_models[
            training.best_model_name
        ]

        x_train = training.x_train
        x_test = training.x_test

        # -------------------------------
        # Select SHAP explainer
        # -------------------------------

        if hasattr(model, "feature_importances_"):

            explainer = shap.TreeExplainer(model)

        elif hasattr(model, "coef_"):

            explainer = shap.LinearExplainer(
                model,
                x_train,
            )

        else:

            raise ValueError(
                f"Unsupported model type: {type(model).__name__}"
            )

        # -------------------------------
        # Generate SHAP explanations
        # -------------------------------

        explanation = explainer(x_test)

        shap_values = explanation.values
        base_values = explanation.base_values

        # -------------------------------
        # Handle binary classification
        # -------------------------------

        if shap_values.ndim == 3:
            shap_values = shap_values[:, :, 1]

        if np.ndim(base_values) > 1:
            base_values = base_values[:, 1]

        # -------------------------------
        # Compute global feature importance
        # -------------------------------

        importance = np.abs(shap_values).mean(axis=0)

        feature_importance = dict(
            sorted(
                zip(
                    x_train.columns,
                    importance,
                ),
                key=lambda item: item[1],
                reverse=True,
            )
        )

        top_features = list(
            feature_importance.keys()
        )[:10]

        return ExplainabilityResult(
            feature_importance=feature_importance,
            top_features=top_features,
            shap_values=shap_values.tolist(),
            expected_value=(
                float(base_values.mean())
                if np.ndim(base_values) > 0
                else float(base_values)
            ),
        )