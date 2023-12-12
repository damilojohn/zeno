import pinecone
import pandas as pd
from tqdm.auto import tqdm
from sentence_transformers import SentenceTransformer
import os

PINECONE_API_KEY = os.environ['PINECONE_API_KEY']
data = pd.read_csv('books.csv')
pinecone.init(
    api_key='2b6ebef8-017d-450f-a640-6ed98916182f',
    environment='us-west1-gcp'
)
index_name = 'zeno'
if index_name not in pinecone.list_indexes():
    pinecone.create_index(
        index_name,
        dimension=384,
        metric='cosine',
    )

index = pinecone.Index(index_name)

device = 'cuda' if torch.cuda.is_available() else 'cpu'
encoder = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
encoder.to(device)


def build_index(data, encoder, batch_size):
    for idx in tqdm(range(0, len(data), batch_size)):
        end_idx = min(idx+batch_size, len(data))
        batch = data[idx:end_idx]
        emb = encoder.encode(batch['description'].tolist()).tolist()
        id = [f'{i}' for i in range(idx, end_idx)]
        metadata = [
            {
                'title': x[0],
                'isbn10': x[1],
                'thumbnail':x[2],
                'description':x[3],
                'authors':x[4],
                'average_rating':x[5],
                'isbn13': x[6],
                'categories':x[7],
                'published_year':x[8]}
                for x in zip(
                    batch['title'],
                    batch['isbn10'],
                    batch['thumbnail'],
                    batch['description'],
                    batch['authors'],
                    batch['average_rating'],
                    batch['isbn13'],
                    batch['categories'],
                    batch['published_year'])
        ]
        to_upsert = list(zip(id, emb, metadata))
        _ = index.upsert(vectors=to_upsert)


build_index(encoder=encoder, data=data, batch_size=64)


def search_query(query):
    query_vec = encoder.encode(query).tolist()
    matches = index.query(query_vec, top_k=10, include_metadata=True)
    result = []
    for meta in matches['matches']:
        result.append(meta)
    return result
