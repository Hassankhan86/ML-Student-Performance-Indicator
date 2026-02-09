import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    """
    DataIngestionConfig stores file paths required
    during the data ingestion process.

    Attributes:
        train_data_path (str): Path where training data will be saved
        test_data_path (str): Path where testing data will be saved
        raw_data_path (str): Path where raw data will be saved
    """
    train_data_path: str = os.path.join('artifacts', "train.csv")
    test_data_path: str = os.path.join('artifacts', "test.csv")
    raw_data_path: str = os.path.join('artifacts', "data.csv")

class DataIngestion:
    """
    DataIngestion class handles the complete data ingestion process:
    - Reading dataset
    - Creating artifacts directory
    - Performing train-test split
    - Saving output files
    """
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        
        logging.info("Entered the data ingestion method or component")
        try:
            # Read dataset from source location
            df = pd.read_csv('notebook\data\stud.csv')
            logging.info('Read the dataset as dataframe')

            # Create artifacts directory if it does not exist
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            # Save raw data
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info("Train test split initiated")
            
            # Split dataset into train and test sets (row-wise split)
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            # Save training dataset
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)

            # Save testing dataset
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Ingestion of the data is completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            # raise custom exception with system info
            raise CustomException(e, sys)
        
if __name__=="__main__":
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()



