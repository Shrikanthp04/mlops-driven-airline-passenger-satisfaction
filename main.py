import sys
from src.airline_passenger_satisfaction.logger import logger
from src.airline_passenger_satisfaction.exception import CustomException
from src.airline_passenger_satisfaction.pipeline.stage_01_data_ingestion_pipeline import DataIngestionTrainingPipeline



STAGE_NAME = "DATA INGESTION STAGE"

try:
    logger.info(f">>>>> {STAGE_NAME} started <<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>> {STAGE_NAME} completed successfully <<<<<")
except Exception as e:
    logger.exception(e)
    raise CustomException(e,sys)