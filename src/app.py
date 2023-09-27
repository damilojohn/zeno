import pinecone 
import os
import logging
import json
from sentence_transformers import SentenceTransformer

encoder = SentenceTransformer(os.getenv('ENCODER_NAME'))

logger = logging.getlogger()
logger.setLevel(logging.info)
logger.info('connecting to vectordb')
pinecone.init(
    api_key=os.getenv('PINECONE_API_KEY'),
    environment=os.getenv('PINECONE_REGION')
)
index_name = 'zeno'
index = pinecone.Index(index_name)
logger.info('connected to index....')


def query_db(index, query):
    query_vec = encoder.encode(query).tolist()
    matches = index.query(query, top_k=10, include_metadata=True)
    results = []
    for result in matches['matches']:
        results.append(result)
    return results


def lambda_handler(event, _context):
    """ Query vector db and return matches"""
    try:
        query = event['body']['query']
    except TypeError:
        query = json.loads(event['body'])
    if query is None:
        return {'statusCode': 400, 'message': 'no input query was provided'}
    results = query_db(index=index, query=query)
    return {
        'body': json.dumps(
            {'books': results}),
        'statusCode': 200,
        'headers':
            {'content-type': 'application/json'}
    }
