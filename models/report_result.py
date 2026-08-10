from pydantic import BaseModel


class ReportResult(BaseModel):
    """
    Stores the generated DataPilot report.
    """

    report_path: str

    report_title: str