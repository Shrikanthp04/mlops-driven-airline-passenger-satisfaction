import sys
from airline_passenger_satisfaction.logger import logger
from airline_passenger_satisfaction.exception import CustomException
from airline_passenger_satisfaction.components.model_trainer import ModelTrainer
from airline_passenger_satisfaction.config.configuration import ConfigurationManager


STAGE_NAME = "Models Training stage"

class ModelsTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.models_trainer()


if __name__=='__main__':
    try:
        logger.info(f">>>>> {STAGE_NAME} started <<<<<")
        obj = ModelsTrainingPipeline()
        obj.main()
        logger.info(f">>>>> {STAGE_NAME} completed <<<<<")
    except Exception as e:
        logger.warning(e)
        raise CustomException(e,sys)