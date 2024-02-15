import os
import sys
import json
import yaml
import joblib
from typing import Any
from pathlib import Path
from box import ConfigBox
from ensure import ensure_annotations
from src.airline_passenger_satisfaction.logger import logger
from src.airline_passenger_satisfaction.exception import CustomException
from sklearn.metrics import precision_score, recall_score, roc_auc_score, accuracy_score

@ensure_annotations
def read_yaml(path_to_yaml:Path)-> ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except Exception as e:
        raise CustomException(e, sys)


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at : {path}")
    

@ensure_annotations
def save_json(path:Path, data:dict):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    
    logger.info(f"json file saved at : {path}")


@ensure_annotations
def load_json(path: Path)-> ConfigBox:
    with open(path) as f:
        content = json.load(f)
    
    logger.info(f"json file loaded successfully from: {Path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(path: Path, data=Any):
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path)-> Any:
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data

@ensure_annotations
def get_size(path: Path) ->str:
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"{size_in_kb} KB" 

def model_evaluation(y_true, y_pred):
    precision = precision_score(y_true, y_pred)
    recall = recall_score(y_true, y_pred)
    acc_score = accuracy_score(y_true, y_pred)
    roc_auc = roc_auc_score(y_true, y_pred)
        
    return precision, recall, roc_auc, acc_score