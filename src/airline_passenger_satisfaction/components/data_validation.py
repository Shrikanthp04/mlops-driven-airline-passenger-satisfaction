import sys
import pandas as pd
from airline_passenger_satisfaction.logger import logger
from airline_passenger_satisfaction.entity.config_entity import DataValidationConfig
from airline_passenger_satisfaction.exception import CustomException

class DataValidation:
    def __init__(self, config: DataValidationConfig) -> None:
        self.config = config

    def validate_all_columns(self) -> bool:
        try:
            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = data.dtypes.to_dict()
            all_schema = self.config.all_schema

            validation_status = True

            with open(self.config.status_file, "w") as f:
                for col, d_type in all_schema.items():
                    if col not in all_cols.keys():
                        logger.warning(f"Column '{col}' was not found in the dataset!")
                        validation_status = False
                    elif data[col].dtype != d_type:
                        logger.warning(f"Column '{col}': Expected type {data[col].dtype}, Found type {d_type}")
                        validation_status = False

                f.write(f"validation status: {validation_status}")

            return validation_status

        except Exception as e:
            raise CustomException(e, sys)
