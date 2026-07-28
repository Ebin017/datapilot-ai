from crew.tools.dataset_tool import DatasetTool
from crew.tools.metadata_tool import MetadataTool
from crew.tools.data_quality_tool import DataQualityTool


DatasetTool().run(
    dataset_path="datasets/employee_attrition.csv",
)

MetadataTool().run(
    file_name="datasets/employee_attrition.csv",
)

result = DataQualityTool().run()

print(result)