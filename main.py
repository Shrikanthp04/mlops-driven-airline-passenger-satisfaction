import sys
from src.airline_passenger_satisfaction.logger import logger
from src.airline_passenger_satisfaction.exception import CustomException
from airline_passenger_satisfaction.pipeline.stage_04_models_training_pipeline import ModelsTrainingPipeline
from airline_passenger_satisfaction.pipeline.stage_05_model_evaluation_pipeline import ModelEvaluationPipeline
from airline_passenger_satisfaction.pipeline.stage_02_data_validation_pipeline import DataValidationTrainingPipeline
from src.airline_passenger_satisfaction.pipeline.stage_01_data_ingestion_pipeline import DataIngestionTrainingPipeline
from airline_passenger_satisfaction.pipeline.stage_03_data_transformation_pipeline import DataTransformationTrainingPipeline



STAGE_NAME = "DATA INGESTION STAGE"

try:
    logger.info(f">>>>> {STAGE_NAME} started <<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>> {STAGE_NAME} completed successfully <<<<<"+'\n\n')
except Exception as e:
    logger.exception(e)
    raise CustomException(e,sys)

STAGE_NAME = "Data Validation stage"

try:
    logger.info(f">>>>> {STAGE_NAME} started <<<<<")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f">>>>> {STAGE_NAME} completed successfully <<<<<"+'\n\n')
except Exception as e:
    logger.exception(e)
    raise CustomException(e,sys)

STAGE_NAME = "Data Transformation stage"

try:
    logger.info(f">>>>> {STAGE_NAME} started <<<<<")
    obj = DataTransformationTrainingPipeline()
    obj.main()
    logger.info(f">>>>> {STAGE_NAME} completed successfully <<<<<"+'\n\n')
except Exception as e:
    logger.exception(e)
    raise CustomException(e,sys)

STAGE_NAME = "Models Training stage"

try:
    logger.info(f">>>>> {STAGE_NAME} started <<<<<")
    obj = ModelsTrainingPipeline()
    obj.main()
    logger.info(f">>>>> {STAGE_NAME} completed successfully <<<<<"+'\n\n')
except Exception as e:
    logger.exception(e)
    raise CustomException(e,sys)

STAGE_NAME = "Models Evaluation stage"

try:
    logger.info(f">>>>> {STAGE_NAME} started <<<<<")
    obj = ModelEvaluationPipeline()
    obj.main()
    logger.info(f">>>>> {STAGE_NAME} completed successfully <<<<<"+'\n\n')
except Exception as e:
    logger.exception(e)
    raise CustomException(e,sys)