import os
import joblib
import pandas as pd
from airline_passenger_satisfaction.entity.config_entity import ModelTrainerConfig
from airline_passenger_satisfaction.logger import logger
from airline_passenger_satisfaction.exception import CustomException

from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.ensemble import RandomForestClassifier
from xgboost.sklearn import XGBClassifier
from sklearn.naive_bayes import GaussianNB
import lightgbm as lgb
from sklearn.ensemble import AdaBoostClassifier

class ModelTrainer:
    def __init__(self, config=ModelTrainerConfig) -> None:
        self.config = config

    def models_trainer(self):
        train_df = pd.read_csv(self.config.train_data_path)

        x_train = train_df.drop(columns=[self.config.target_column])
        y_train = train_df[self.config.target_column]


        models = {
            "Logistic Regression": LogisticRegression(),
            "KNeighbors Classifier": KNeighborsClassifier(),
            "Decision Tree Classifier": DecisionTreeClassifier(),
            "Naive Bayes": GaussianNB(),
            "Support Vector Machine": SVC(),
            "Gradient Descent": SGDClassifier(),
            "Random Forest Classifier": RandomForestClassifier(),
            "Xgboost Classifier": XGBClassifier(),
            "Adaboost Classifier": AdaBoostClassifier(),
            "Gradient Boosting Blassifier": GradientBoostingClassifier(),
            "Lightgbm": lgb.LGBMClassifier()
        }

        for model_name, model_instance in models.items():
            model_instance.fit(x_train, y_train)
   
            joblib.dump(model_instance, f'{self.config.root_dir}/{model_name}.joblib')
            print(f"Model '{model_name}' saved to '{self.config.root_dir}/{model_name}.joblib'.")
            logger.info(f"Model '{model_name}' saved to '{self.config.root_dir}/{model_name}.joblib'.")