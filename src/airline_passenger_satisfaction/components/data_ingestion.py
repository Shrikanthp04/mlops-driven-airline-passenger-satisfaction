import os
import zipfile
from pathlib import Path
import urllib.request as request
from src.airline_passenger_satisfaction.logger import logger
from src.airline_passenger_satisfaction.utils.common import get_size
from airline_passenger_satisfaction.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig) -> None:
        self.config = config
    

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers =  request.urlretrieve(
                url = self.config.source_url,
                filename=self.config.local_data_file
            )

            logger.info(f"{filename} download with following info:\n{headers}")
        else:
            logger.info(f"file already exists of size: {get_size(Path(self.config.local_data_file))}")


    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)