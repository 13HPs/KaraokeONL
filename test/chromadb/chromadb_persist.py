import chromadb

from chromadb.utils import embedding_functions

default_emb = embedding_functions.DefaultEmbeddingFunction()
chroma_client = chromadb.PersistentClient(path="./test/chromadb/chromadb_db")

# collection = chroma_client.create_collection("example_collection", embedding_function=default_emb)
collection = chroma_client.get_collection("example_collection")

documents = [
    {
        "id": "670a4c8a8509bbcdebd7451d",
        "content": "Trịnh Trần Phương Tuấn",
        "metadata": {"username": "J97"}
    },
    {
        "id": "670a479d7442a0b667e9815a",
        "content": "Nguyen Thanh Tung",
        "metadata": {"username": "sontung"}
    },
    {
        "id": "670a4e5cd15b6b348a33e039",
        "content": "123",
        "metadata": {"username": "DALAB"}
    },
    {
        "id": "670a4e5cd15b6b348a33e03a",
        "content": "John doe123",
        "metadata": {"username": "MTP456"}
    },
]

# Upserting documents into the collection
for doc in documents:
    collection.upsert(
        ids=[doc["id"]],
        documents=[doc["content"]],
        metadatas=[doc["metadata"]]
    )
query_text = "DALAB"
results = collection.query(
    query_texts=[query_text],
    n_results=5
)
print(results)
for idx, document in enumerate(results["documents"][0]):
    doc_id = results["ids"][0][idx]
    distance = results["distances"][0][idx]
    print(f"For the query: {query_text},Document ID: {doc_id}, Distance: {distance}")
