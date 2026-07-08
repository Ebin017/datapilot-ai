from pathlib import Path

from services.dataset.dataset_service import DatasetService
from services.dataset.metadata_service import (
    MetadataService,
)
from services.dataset.data_quality_service import DataQualityService

def main() -> None:
    dataset_service = DatasetService()
    metadata_service = MetadataService()
    data_quality_service = DataQualityService()

    dataset_path = Path("data/customer_churn.csv")

    dataframe = dataset_service.load_dataset(dataset_path)

    dataset_info = metadata_service.extract(
        dataframe,
        dataset_path.name,
    )

    data_quality = data_quality_service.analyze(dataframe)

    print("\nDataset Information")
    print("-" * 40)
    print(dataset_info)

    print("\nFirst Five Rows")
    print("-" * 40)
    print(dataframe.head())

    print("\nData Quality")
    print("-" * 40)
    print(data_quality)

if __name__ == "__main__":
    main()