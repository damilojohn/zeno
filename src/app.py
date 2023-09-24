import pinecone 
import os 
import pandas as pd 
import logging 

logger = logging.getlogger()
logger.setLevel(logging.info)

def lambda_handler(event,_context):
    query = event['query']
    