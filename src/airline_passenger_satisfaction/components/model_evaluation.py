import os
import joblib
import pandas as pd
from pathlib import Path
from airline_passenger_satisfaction.logger import logger
from airline_passenger_satisfaction.utils.common import model_evaluation, save_json
from airline_passenger_satisfaction.config.configuration import ModelEvaluationConfig


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig) -> None:
        self.config = config
    
    def identify_best_model(self):
        test_df = pd.read_csv(self.config.test_data_path)
        valid_df = pd.read_csv(self.config.valid_data_path)

        x_test = test_df.drop(columns= self.config.target_column)
        y_test = test_df[self.config.target_column]

        x_valid = valid_df.drop(columns=self.config.target_column)
        y_valid = valid_df[self.config.target_column]


        model_list = []
        accuracy_score_list = []

        for model_file in os.listdir(self.config.models_path):
            if model_file.endswith('.joblib'):
                model_path = Path(os.path.join(self.config.models_path, model_file))
                model = joblib.load(model_path)

                y_test_pred = model.predict(x_test)
                y_valid_pred = model.predict(x_valid)

                logger.info(f"{'>'*5} {model_file.replace('.joblib','')} {'<'*5}".center(64))
                logger.info("*** Test Dataset ***".center(64))
                logger.info(" Precision \t Recall \tROC-AUC Score \t  Accuracy Score ")
                logger.info('-' * 64)
                test_precision, test_recall, test_roc_auc, test_acc_score = model_evaluation(y_test, y_test_pred)
                logger.info(f" {test_precision:.2%}\t  {test_recall:.2%}\t  {test_roc_auc:.2%}\t\t {test_acc_score:.2%}")

                logger.info("*** Validation Dataset ***".center(64))
                logger.info(" Precision \t Recall \tROC-AUC Score \t  Accuracy Score ")
                logger.info('-' * 64)
                precision, recall, roc_auc, acc_score = model_evaluation(y_valid, y_valid_pred)
                logger.info(f" {precision:.2%}\t  {recall:.2%}\t  {roc_auc:.2%}\t\t {acc_score:.2%}"+'\n')
        
                model_list.append(model_file)
                avg_acc_score = (acc_score+test_acc_score)/2
                accuracy_score_list.append(avg_acc_score)

        best_model_index = accuracy_score_list.index(max(accuracy_score_list))
        best_model_name = model_list[best_model_index].replace('.joblib','')
        best_model_score = accuracy_score_list[best_model_index]


        if best_model_score > 0.6:
            logger.info(f"Model: {best_model_name} with a best Accuracy Score : {best_model_score:.2%}")
            save_json(path=Path(self.config.metrics_file_name), data={"model": best_model_name,"accuracy_score": best_model_score})

            with open(f'{self.config.models_path}/best_model.txt', 'w') as file:
                file.write(f"Model : {best_model_name} with Accuracy Score: {best_model_score:.2%}") 
                logger.info(f"Best model: {best_model_name} saved as Best_model.joblib file format")
                model = joblib.load(f'{self.config.models_path}/{best_model_name}.joblib')
                joblib.dump(model, f'{self.config.models_path}/Best_model.joblib')

        else:
            logger.info("No model with accuracy score > 60% found. Skipping saving.")