from pathlib import Path
import logging
import os

PROJECT_NAME = "airline-passenger-satisfaction"

file_paths = [
    ".github/workflows/main.yaml",
    "research/trails.ipynb",
    "templates/index.html",
    "statics/style.css",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "setup.py",
    "main.py",
    "app.py",
    "requirement.txt",
    "Dockerfile",
    f"src/{PROJECT_NAME}/__init__.py",
    f"src/{PROJECT_NAME}/config/__init__.py",
    f"src/{PROJECT_NAME}/config/configuration.py",
    f"src/{PROJECT_NAME}/components/__init__.py",
    f"src/{PROJECT_NAME}/entity/__init__.py",
    f"src/{PROJECT_NAME}/entity/config_entity.py",
    f"src/{PROJECT_NAME}/utils/__init__.py",
    f"src/{PROJECT_NAME}/utils/common.py",
    f"src/{PROJECT_NAME}/constants/__init__.py",
    f"src/{PROJECT_NAME}/pipeline/__init__.py",
    f"src/{PROJECT_NAME}/logger.py",
    f"src/{PROJECT_NAME}/exception.py",
]

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR,"project_structure.log")
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format="[%(asctime)s] : [%(module)s] : [%(message)s]")

logging.info(f"{'>'*5} Project Structure Creating {'<'*5}")

for file_path in file_paths:
    file_path = Path(file_path)
    directory, file_name = os.path.split(file_path)

    if directory!="":
        os.makedirs(directory, exist_ok=True)
        logging.info(f"Creating directory: {directory} for the file: {file_name}")
    
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path)==0):
        with open(file_path, 'w') as f:
            logging.info(f"Creating empty file: {file_path}")
            pass
    else:
        logging.info(f"file: {file_path} is already exists")

logging.info(f"{'>'*5} Project Structure Created Successfully {'<'*5}")