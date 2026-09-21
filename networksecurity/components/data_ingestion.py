import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging_config.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.artifact_ingestion import DataIngestionArtifact


class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def initiate_data_ingestion(self):
        try:
            logging.info("Entered the data ingestion method")

            # apne dataset ka sahi path daalo
            df = pd.read_csv("Network_Data/phisingData.csv")

            # raw data save karo
            feature_store_path = self.data_ingestion_config.feature_store_file_path
            os.makedirs(os.path.dirname(feature_store_path), exist_ok=True)
            df.to_csv(feature_store_path, index=False, header=True)

            # train-test split
            train_set, test_set = train_test_split(
                df, test_size=self.data_ingestion_config.train_test_split_ratio
            )

            train_path = self.data_ingestion_config.training_file_path
            test_path = self.data_ingestion_config.testing_file_path
            os.makedirs(os.path.dirname(train_path), exist_ok=True)

            train_set.to_csv(train_path, index=False, header=True)
            test_set.to_csv(test_path, index=False, header=True)

            logging.info("Data ingestion completed")

            return DataIngestionArtifact(
                trained_file_path=train_path,
                test_file_path=test_path,
            )
        except Exception as e:
            raise NetworkSecurityException(e, sys)