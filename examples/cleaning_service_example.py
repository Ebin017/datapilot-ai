from pathlib import Path

from context.project_context import ProjectContext

from services.dataset.dataset_service import DatasetService
from services.dataset.metadata_service import MetadataService
from services.dataset.data_quality_service import DataQualityService

from services.cleaning.cleaning_strategy_service import (
    CleaningStrategyService,
)
from services.cleaning.data_cleaning_service import (
    DataCleaningService,
)


def main():

    # Services
    dataset_service = DatasetService()
    metadata_service = MetadataService()
    data_quality_service = DataQualityService()

    cleaning_strategy_service = CleaningStrategyService()
    data_cleaning_service = DataCleaningService()

    # Load dataset
    dataframe = dataset_service.load_dataset(
        Path("data/cleaning1.csv"),
    )

    # Metadata
    dataset_info = metadata_service.extract(
        dataframe=dataframe,
        file_name="employee_attrition.csv",
    )

    # Data quality
    data_quality = data_quality_service.analyze(
        dataframe,
    )

    # Create shared context
    context = ProjectContext(
        dataframe=dataframe,
        dataset_info=dataset_info,
        data_quality=data_quality,
    )

    # Generate cleaning plan
    cleaning_plan = cleaning_strategy_service.generate_plan(
        context,
    )

    # Execute cleaning
    cleaning_result = data_cleaning_service.clean(
        context,
        cleaning_plan,
    )

    print("\nCleaning Plan")
    print("-" * 40)
    print(cleaning_plan)

    print("\nCleaning Result")
    print("-" * 40)
    print(cleaning_result)

    print("\nCleaned Dataset")
    print("-" * 40)
    print(context.dataframe.head())


if __name__ == "__main__":
    main()