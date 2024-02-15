# mlops-driven-airline-passenger-satisfaction

## Project Workflow

1. update config.yaml
2. update schema.yaml
3. update params.yaml
4. update the entity
5. update the configuration manager in src config
6. update the components
7. update the pipeline
8. update the dvc.yaml
9. update the main.py
10. update the app.py


# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/Shrikanthp04/mlops-driven-airline-passenger-satisfaction
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n env python=3.11 -y
```

```bash
conda activate env
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```



## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)


##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/Shrikanthp04/mlops-driven-airline-passenger-satisfaction.mlflow \
MLFLOW_TRACKING_USERNAME=Shrikanthp04 \
MLFLOW_TRACKING_PASSWORD=271b57f7e54d3a30da05ccc8658547a1f2188b2d \
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/Shrikanthp04/mlops-driven-airline-passenger-satisfaction.mlflow

export MLFLOW_TRACKING_USERNAME=Shrikanthp04

export MLFLOW_TRACKING_PASSWORD=271b57f7e54d3a30da05ccc8658547a1f2188b2d

```
## About MLflow 
MLflow

 - Its Production Grade
 - Trace all of your expriements
 - Logging & tagging your model