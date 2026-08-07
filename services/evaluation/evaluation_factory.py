from models.enums.problem_type import ProblemType

from services.evaluation.evaluators.classification_evaluator import (
    ClassificationEvaluator,
)

from services.evaluation.evaluators.regression_evaluator import (
    RegressionEvaluator,
)


class EvaluationFactory:
    """
    Creates the appropriate evaluator based on the problem type.
    """

    @staticmethod
    def create(
        problem_type: ProblemType,
    ):

        if problem_type == ProblemType.CLASSIFICATION:
            return ClassificationEvaluator()

        if problem_type == ProblemType.REGRESSION:
            return RegressionEvaluator()

        raise ValueError(
            f"Unsupported problem type: {problem_type}"
        )