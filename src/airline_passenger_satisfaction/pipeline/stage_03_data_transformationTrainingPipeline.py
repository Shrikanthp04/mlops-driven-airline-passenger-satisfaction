import sys
from airline_passenger_satisfaction.logger import logger
from airline_passenger_satisfaction.components.data_transformation import DataTransformation
from airline_passenger_satisfaction.config.configuration import ConfigurationManager
from airline_passenger_satisfaction.exception import CustomException


STAGE_NAME = "Data Transformation stage"

class DataTransformationTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        num_cols, cat_cols = data_transformation.separate_numeric_categorical_columns()
        data_transformation.handling_missing_data(numeric_cols=num_cols)
        num_cols, cat_cols = data_transformation.drop_unwanted_columns(['ID'], num_cols, cat_cols)
        data_transformation.feature_scaling_numerical_columns(num_cols=num_cols)
        num_cols,cat_cols = data_transformation.feature_scaling_categorical_columns(cat_cols=cat_cols,num_cols=num_cols)
        data_transformation.mapping_target_column()
        data_transformation.train_test_spliting()


if __name__=='__main__':
    try:
        logger.info(f">>>>> {STAGE_NAME} started <<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>> {STAGE_NAME} completed <<<<<")
    except Exception as e:
        logger.warning(e)
        raise CustomException(e,sys)