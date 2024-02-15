from src.airline_passenger_satisfaction.utils.common import read_yaml, create_directories
from airline_passenger_satisfaction.entity.config_entity import DataIngestionConfig, DataTransformationConfig, DataValidationConfig, ModelEvaluationConfig, ModelTrainerConfig
from src.airline_passenger_satisfaction.constants import *

class ConfigurationManager:
    def __init__(self,
                 config_filepath = CONFIG_FILE_PATH,
                 params_filepath = PARAMS_FILE_PATH,
                 schema_filepath = SCHEMA_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories([self.config.artifacts_root]) 

    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir,
            source_url = config.source_url,
            local_data_file = config.local_data_file,
            unzip_dir = config.unzip_dir
        )

        return data_ingestion_config
    
    def get_data_validation(self)-> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir= config.root_dir,
            status_file= config.status_file,
            unzip_data_dir= config.unzip_data_dir,
            all_schema=schema,
        )        

        return data_validation_config
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation
        schema = self.schema.TARGET_COLUMN

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir= config.root_dir,
            data_path= config.data_path,
            target_column=schema,
        )        

        return data_transformation_config
    
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        schema = self.schema.TARGET_COLUMN

        create_directories([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir= config.root_dir,
            train_data_path= config.train_data_path,
            target_column= schema.name
        )

        return model_trainer_config
    
    def get_model_evaluation(self)-> ModelEvaluationConfig:
        config = self.config.model_evaluation
        params = self.params
        schema = self.schema.TARGET_COLUMN

        create_directories([config.root_dir])

        model_evaluation_config = ModelEvaluationConfig(
            root_dir= config.root_dir,
            test_data_path= config.test_data_path,
            valid_data_path= config.valid_data_path,
            models_path= config.models_path,
            best_model_path= config.best_model_path,
            target_column= schema.name,
            metrics_file_name= config.metric_file_name,
        ) 

        return model_evaluation_config