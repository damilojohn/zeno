from pinecone.grpc import PineconeGRPC as pinecone
from pinecone import ServerlessSpec
import os
import logging
import json
from sentence_transformers import SentenceTransformer

encoder = SentenceTransformer('mixedbread-ai/mxbai-embed-large-v1')

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.info('connecting to vectordb')

PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')

pc = pinecone(
    api_key=PINECONE_API_KEY
)
print(PINECONE_API_KEY)
index_name = 'zeno'
index = pc.Index(index_name)
logger.info('connected to vectordb....')


def query_db(index, query):
    logger.info('generating query embeddings....')
    query_vec = encoder.encode(query).tolist()
    logger.info('performing semantic search...')
    matches = index.query(query_vec, top_k=10, include_metadata=True)
    matches = matches['matches']
    response = []
    for i in range(len(matches)):
        response.append(matches[i]['metadata'])
    return response


def lambda_handler(event, _context):
    """ Query vector db and return matches"""
    try:
        query = event['body']['query']
    except TypeError:
        request = json.loads(event['body'])
        query = request['query']
    if query is None:
        return {'statusCode': 400, 'message': 'no input query was provided'}
    response = query_db(index=index, query=query)
    return {
        'body': json.dumps(
            {'books': response}),
        'statusCode': 200,
        'headers':
            {'content-type': 'application/json',
             'Access-Control-Allow-Origin': '*',
             'Access-Control-Allow-Methods': 'POST,OPTION'}
    }
