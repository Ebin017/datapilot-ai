from context.project_context import ProjectContext

from services.dataset.dataset_service import DatasetService
from services.dataset.metadata_service import MetadataService
from services.dataset.data_quality_service import DataQualityService
from services.eda_visualization.eda_visualization_service import (
    EDAVisualizationService,
)


def main():

    dataset_service = DatasetService()
    metadata_service = MetadataService()
    data_quality_service = DataQualityService()
    visualization_service = EDAVisualizationService()

    # Load dataset
    dataframe = dataset_service.load_dataset(
        "data/employee_attrition.csv",
    )

    # Extract metadata
    dataset_info = metadata_service.extract(
        dataframe,
        "employee_attrition.csv",
    )

    # Analyze data quality
    data_quality = data_quality_service.analyze(
        dataframe,
    )

    # Create workflow context
    context = ProjectContext(
        dataframe=dataframe,
        dataset_info=dataset_info,
        data_quality=data_quality,
    )

    # Generate visualizations
    result = visualization_service.generate(
        context,
    )

    print("\nGenerated Charts")
    print("-" * 40)

    for chart in result.chart_paths:
        print(chart)


if __name__ == "__main__":
    main()