import chromadb

chroma_client = chromadb.Client()
from chromadb.utils import embedding_functions

default_emb = embedding_functions.DefaultEmbeddingFunction()
collection_name = "test_collection"

collection = chroma_client.get_or_create_collection(collection_name, embedding_function=default_emb)

documents = [
    {"id": "doc1", "name": "John doe", "email": "john.doe@example.com"},
    {"id": "doc2", "name": "John Doe1", "email": "john.doe1@example.com"},
    {"id": "doc3", "name": "John Doe2", "email": "john.doe2@example.com"}
]

for document in documents:
    collection.upsert(ids=document["id"], documents=[document["name"]])

query = "TranLeMinh"

results = collection.query(
    query_texts=[query],
    n_results=3
)
for idx, document in enumerate(results["documents"][0]):
    doc_id = results["ids"][0][idx]
    distance = results["distances"][0][idx]
    print(f"For the query: {query},Document ID: {doc_id}, Distance: {distance}")
