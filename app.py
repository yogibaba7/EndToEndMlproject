from src.E2EMlProject.logger import logging
from src.E2EMlProject.exception import CustomException
import sys 
from src.E2EMlProject.components.data_ingestion import DataIngestion


if __name__=="__main__":
    logging.info("The Excecution has started")

    try:
        dataingestion = DataIngestion()
        x,y,z = dataingestion.initiate_data_ingestion()
        print(x)
        print(y)
        print(z)
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)
