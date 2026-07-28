from crew.tools.dataset_tool import DatasetTool
from crew.tools.metadata_tool import MetadataTool
from crew.tools.data_quality_tool import DataQualityTool
from crew.tools.cleaning_strategy_tool import (
    CleaningStrategyTool,
)


DatasetTool().run(
    dataset_path="datasets/cleaning1.csv",
)

MetadataTool().run(
    file_name="datasets/cleaning1.csv",
)

DataQualityTool().run()

result = CleaningStrategyTool().run()

print(result)