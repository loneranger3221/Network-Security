import os
import sys 
import json 

'''dotenv is being used to load the environmental variables '''
from dotenv import load_dotenv
load_dotenv()

MONGODB_URI=os.getenv('MONGODB_URI')
print(MONGODB_URI)

'''certifi is used to ensure the connection is secure and valid'''
import certifi 
ca=certifi.where()

'''Now we will read our dataset from local source-> Main packages'''
import pandas as pd
import numpy as np

from src.logging.logger import logging
from src.exception.exception import CustomException

'''For creating client for all CRUD operation'''
import pymongo
from pymongo import MongoClient

'''ETL pipeline'''
class NetworkDataExtract:
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise CustomException(e,sys)
    
    def csv_to_json(self,file_path):
        try:
            '''Loading and cleaning the dataset'''
            df=pd.read_csv(file_path)
            df.reset_index(drop=True,inplace=True)
            df = df.replace({np.nan: None})
            
            '''converting the df to a list of dictionary/key-val pairs for mongodb'''
            records = df.to_dict(orient="records")
            return records
        except Exception as e:
            raise CustomException(e,sys)
        
    def insert_data_mongodb(self,records,database_name,collection_name):
        '''collection is like a table in a database'''
        try:
            self.records=records
            self.database_name=database_name
            self.collection_name=collection_name
                
            '''Now we will insert the records into the collection in the database using a client'''
            client=pymongo.MongoClient(MONGODB_URI, tlsCAFile=ca)
            db=client[self.database_name]
            col=db[self.collection_name]
            
            '''Inserting records'''
            if self.records:
                result=col.insert_many(self.records)
                return f"Successfully inserted {len(result.inserted_ids)} documents."
        except Exception as e:
            raise CustomException(e,sys)


'''Executing the above operations '''
if __name__=="__main__":
    obj=NetworkDataExtract()
    
    RECORDS=obj.csv_to_json(file_path='Notebooks/Phishing_Dataset.csv')
    DATABASE=os.getenv('MONGODB_DATABASE')
    COLLECTION=os.getenv('MONGODB_COLLECTION')
    
    print(obj.insert_data_mongodb(RECORDS,DATABASE,COLLECTION))