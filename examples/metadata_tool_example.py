from crew.tools.dataset_tool import DatasetTool
from crew.tools.metadata_tool import MetadataTool

DatasetTool().run(
    dataset_path="datasets/employee_attrition.csv",
)

result = MetadataTool().run(
    file_name="datasets/employee_attrition.csv",
)

print(result)