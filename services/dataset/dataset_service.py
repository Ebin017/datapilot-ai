from pathlib import Path

import pandas as pd
from pandas.errors import EmptyDataError, ParserError



class DatasetService:
    """
    Service responsible for loading datasets
    and extracting basic metadata.
    """

    def _validate_file(self, file_path: Path) -> None:
        """
        Validate that the dataset file exists and is a CSV.
        """

        if not file_path.exists():
            raise FileNotFoundError(f"Dataset not found: {file_path}")

        if file_path.suffix.lower() != ".csv":
            raise ValueError("Only CSV files are supported in Version 1.")

    def load_dataset(
        self,
        file_path: str | Path,
    ) -> pd.DataFrame:

        file_path = Path(file_path)

        self._validate_file(file_path)

        try:
            dataframe = pd.read_csv(file_path)

        except EmptyDataError:
            raise ValueError("The dataset is empty.")

        except ParserError:
            raise ValueError("The CSV file could not be parsed.")

        return dataframe

    
# TODO:
# Support Excel and Parquet in future versions.