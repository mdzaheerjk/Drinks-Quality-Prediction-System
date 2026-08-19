import os
from mlProject import logger
import pandas as pd
from sklearn.model_selection import train_test_split
from mlProject.entity.config_entity import DataTransformatinConfig

class DataTransformation:
    def __init__(self,config:DataTransformatinConfig):
        self.config=config

    def train_test_spliting(self):
        data=pd.read_csv(self.config.data_path)

        train,test=train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir,"train.csv"),index=False)
        test.to_csv(os.path.join(self.config.root_dir,"test.csv"),index=False)

        logger.info("Splitted data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)