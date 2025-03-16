from src.E2EMlProject.logger import logging
from src.E2EMlProject.exception import CustomException
import sys 


if __name__=="__main__":
    logging.info("The Excecution has started")

    try:
        a = 1/0
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)
