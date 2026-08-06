import logging

from sklearn.model_selection import train_test_split

from context.project_context import ProjectContext
from models import ModelTrainingResult

from services.training.model_factory import ModelFactory
from services.evaluation.metric_factory import MetricFactory

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

        metric = MetricFactory.create(plan.evaluation_metric,)

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

            if plan.problem_type.value == "classification":

                if plan.evaluation_metric == "roc_auc":

                    probabilities = model.predict_proba(
                        x_test,
                    )[:, 1]

                    score = metric(
                        y_test,
                        probabilities,
                    )

                else:

                    score = metric(
                        y_test,
                        predictions,
                    )

            else:

                score = metric(
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

        best_model =  trained_models[best_model_name]

        return ModelTrainingResult(
            trained_models=trained_models,
            evaluation_scores=evaluation_scores,
            best_model_name=best_model_name,
            best_score=evaluation_scores[best_model_name],
            best_model=best_model,
            x_train=x_train,
            x_test=x_test,
            y_train=y_train,
            y_test=y_test,
        )