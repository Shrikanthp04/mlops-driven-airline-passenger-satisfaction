import sys
from airline_passenger_satisfaction.logger import logger
from airline_passenger_satisfaction.exception import CustomException
from airline_passenger_satisfaction.components.data_ingestion import DataIngestion
from airline_passenger_satisfaction.config.configuration import ConfigurationManager

STAGE_NAME = "DATA INGESTION STAGE"

class DataIngestionTrainingPipeline:
    def  __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
        

if __name__=='__main__':
    try:
        logger.info(f">>>>> {STAGE_NAME} started <<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>> {STAGE_NAME} completed successfully <<<<<")
    except Exception as e:
        logger.exception(e)
        raise CustomException(e,sys)