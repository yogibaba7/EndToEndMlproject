import os 
import sys 
from src.E2EMlProject.exception import CustomException
from src.E2EMlProject.logger import logging
import pandas as pd
from dotenv import load_dotenv
import pymysql

load_dotenv()

host = os.getenv('host')
user = os.getenv('user')
password = os.getenv('password')
db = os.getenv('db')

# read sql data

def read_sql_data():

    logging.info('Reading sql database started')
    try:
        mydb = pymysql.connect(
                    host=host,
                    user = user,
                    password = password,
                    db=db
                )

        logging.info('connection established with database')
        df = pd.read_sql_query('select * from students',mydb)
        print(df)

        return df


    except Exception as e:
        raise CustomException(e,sys)

