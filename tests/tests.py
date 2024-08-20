from pinecone.grpc import PineconeGRPC as pinecone
from pinecone import ServerlessSpec


PINECONE_API_KEY = '2b6ebef8-017d-450f-a640-6ed98916182f'

pc = pinecone(
    api_key=PINECONE_API_KEY
)
index_name = 'zeno'
index = pc.Index(index_name)
print(index.describe_index_stats())
