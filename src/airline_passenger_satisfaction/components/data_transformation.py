import os
import sys
import pandas as pd
from ensure import ensure_annotations
from sklearn.exceptions import NotFittedError
from airline_passenger_satisfaction.entity.config_entity import DataTransformationConfig
from airline_passenger_satisfaction.logger import logger
from airline_passenger_satisfaction.exception import CustomException
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder


class DataTransformation:
    def __init__(self, config: DataTransformationConfig) -> None:
        self.config = config
        self.target_column = config.target_column.name
        self.data = pd.read_csv(self.config.data_path)

    def separate_numeric_categorical_columns(self):
        numeric_columns = self.data.select_dtypes(exclude='object').columns.tolist()
        categorical_columns = self.data.select_dtypes('object').columns.tolist()

        if self.target_column in categorical_columns:
            categorical_columns.remove(self.target_column)
        
        return numeric_columns, categorical_columns
    
    @ensure_annotations
    def handling_missing_data(self, numeric_cols: list):
        missing_columns = [col for col in self.data.columns if self.data[col].isna().sum() != 0]

        if len(missing_columns) != 0:
            for col in missing_columns:
                if col in numeric_cols:
                    self.data[col] = SimpleImputer(strategy='median').fit_transform(self.data[[col]])
                else:
                    self.data[col] = SimpleImputer(strategy='most_frequent').fit_transform(self.data[[col]])

    @ensure_annotations
    def drop_unwanted_columns(self, cols_ls: list, num_cols: list, cat_cols: list):
        columns_to_drop = [col for col in cols_ls if col in self.data.columns]
        
        if columns_to_drop:
            for col in columns_to_drop:
                if col in num_cols:
                    num_cols.remove(col)
                elif col in cat_cols:
                    cat_cols.remove(col)
                    
            self.data.drop(columns=columns_to_drop, inplace=True)

        return num_cols, cat_cols
    
    @ensure_annotations
    def feature_scaling_numerical_columns(self,num_cols: list):
        scaler = StandardScaler()
        self.data[num_cols] = scaler.fit_transform(self.data[num_cols])

    
    @ensure_annotations
    def feature_scaling_categorical_columns(self, cat_cols: list, num_cols: list):
        encoder = OneHotEncoder(handle_unknown='ignore').fit(self.data[cat_cols])
        encoded_data = encoder.transform(self.data[cat_cols])

        encoded_cols = encoder.get_feature_names_out()
        encoded_df = pd.DataFrame(encoded_data.toarray(), columns=encoded_cols)

        self.data = pd.concat([self.data, encoded_df], axis=1)
    
        num_cols, cat_cols = self.drop_unwanted_columns(cols_ls=cat_cols, num_cols=num_cols, cat_cols=cat_cols)
    
        return num_cols, cat_cols



    def mapping_target_column(self):
        if self.target_column in self.data.columns:
            self.data[self.target_column] = self.data[self.target_column].map({'Neutral or Dissatisfied': 0, 'Satisfied': 1})
        else:
            logger.warning(f"Target column '{self.target_column}' not found in the DataFrame.")
    
    def train_test_spliting(self):
        train, test = train_test_split(self.data, test_size=0.25, random_state=42)
        train, valid = train_test_split(self.data, test_size=0.20, random_state=42)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)
        valid.to_csv(os.path.join(self.config.root_dir, "valid.csv"), index=False)

        logger.info("Spliting Dataset into training, testing and validate sets")
        logger.info(f"Train Dataset shape : {train.shape}")
        logger.info(f"Test Dataset shape : {test.shape}")
        logger.info(f"valid Dataset shape : {valid.shape}")