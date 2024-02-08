import sys
from airline_passenger_satisfaction.logger import logger
from airline_passenger_satisfaction.components.data_validation import DataValidation
from airline_passenger_satisfaction.config.configuration import ConfigurationManager
from airline_passenger_satisfaction.exception import CustomException


STAGE_NAME = "Data Validation stage"


class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_columns()


if __name__=='__main__':
    try:
        logger.info(f">>>>> {STAGE_NAME} stated <<<<<")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>>> {STAGE_NAME} Completed <<<<<")
    except Exception as e:
        logger.exception(e)
        raise CustomException(e,sys)