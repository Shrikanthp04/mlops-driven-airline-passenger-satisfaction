import sys
from airline_passenger_satisfaction.pipeline.stage_03_data_transformationTrainingPipeline import DataTransformationTrainingPipeline
from src.airline_passenger_satisfaction.logger import logger
from src.airline_passenger_satisfaction.exception import CustomException
from airline_passenger_satisfaction.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
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

STAGE_NAME = "Data Validation stage"

try:
    logger.info(f">>>>> {STAGE_NAME} started <<<<<")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f">>>>> {STAGE_NAME} completed successfully <<<<<")
except Exception as e:
    logger.exception(e)
    raise CustomException(e,sys)

STAGE_NAME = "Data Transformation stage"

try:
    logger.info(f">>>>> {STAGE_NAME} started <<<<<")
    obj = DataTransformationTrainingPipeline()
    obj.main()
    logger.info(f">>>>> {STAGE_NAME} completed successfully <<<<<")
except Exception as e:
    logger.exception(e)
    raise CustomException(e,sys)