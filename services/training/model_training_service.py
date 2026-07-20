import logging

from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split

from context.project_context import ProjectContext
from models import ModelTrainingResult

from services.training.model_factory import ModelFactory


logger = logging.getLogger(__name__)


class ModelTrainingService:
    """
    Trains machine learning models.
    """

    def train(
        self,
        context: ProjectContext,
    ) -> ModelTrainingResult:

        features = context.feature_engineering_result.features
        target = context.feature_engineering_result.target

        plan = context.analysis_plan

        x_train, x_test, y_train, y_test = train_test_split(
            features,
            target,
            test_size=plan.train_test_split,
            random_state=plan.random_state,
            stratify=target if plan.stratify_split else None,
        )

        trained_models = {}
        evaluation_scores = {}

        for candidate in plan.candidate_models:

            try:
                model = ModelFactory.create(
                    candidate.name,
                )

            except ValueError:

                logger.warning(
                    "Skipping unsupported model: %s",
                    candidate.name,
                )

                continue

            model.fit(
                x_train,
                y_train,
            )

            predictions = model.predict(
                x_test,
            )

            score = f1_score(
                y_test,
                predictions,
            )

            trained_models[candidate.name] = model
            evaluation_scores[candidate.name] = score

        if not trained_models:
            raise ValueError(
                "No supported models were trained."
            )

        best_model_name = max(
            evaluation_scores,
            key=evaluation_scores.get,
        )

        return ModelTrainingResult(
            trained_models=trained_models,
            evaluation_scores=evaluation_scores,
            best_model_name=best_model_name,
            best_score=evaluation_scores[best_model_name],
            x_train=x_train,
            x_test=x_test,
            y_train=y_train,
            y_test=y_test,
        )