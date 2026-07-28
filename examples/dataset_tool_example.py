from crew.tools.dataset_tool import DatasetTool

tool = DatasetTool()

result = tool.run(
    dataset_path="data/employee_attrition.csv",
)

print(result)