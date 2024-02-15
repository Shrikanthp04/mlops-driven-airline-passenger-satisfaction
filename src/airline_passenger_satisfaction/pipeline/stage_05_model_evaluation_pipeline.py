import sys
from airline_passenger_satisfaction.components.model_evaluation import ModelEvaluation
from airline_passenger_satisfaction.config.configuration import ConfigurationManager
from airline_passenger_satisfaction.exception import CustomException
from airline_passenger_satisfaction.logger import logger


STAGE_NAME = "Models Evaluation stage"

class ModelEvaluationPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.identify_best_model()


if __name__=='__main__':
    try:
        logger.info(f">>>>> {STAGE_NAME} started <<<<<")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>>> {STAGE_NAME} completed <<<<<")
    except Exception as e:
        logger.warning(e)
        raise CustomException(e,sys)