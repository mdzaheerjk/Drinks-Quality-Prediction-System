import os
import urllib.request as requests
import zipfile
from mlProject import logger
from mlProject.utils.common import get_size
from pathlib import Path
from mlProject.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            try:
                filename,headers=requests.urlretrieve(
                    url=self.config.source_URL,
                    filename=self.config.local_data_file
                )
                logger.info(f"{filename} Download! With following info: \n {headers}")
            except Exception as e:
                logger.warning(f"Failed to download from source_URL ({e}). Using local fallback data/Drinks-data.zip.")
                local_fallback = Path("data/Drinks-data.zip")
                if local_fallback.exists():
                    import shutil
                    shutil.copy(local_fallback, self.config.local_data_file)
                    logger.info(f"Copied local data file from {local_fallback} to {self.config.local_data_file}")
                else:
                    raise e
        else:
            logger.info(f"File already exists of size : {get_size(Path(self.config.local_data_file))}")


    def extract_zip_file(self):
        unzip_path=self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_path)