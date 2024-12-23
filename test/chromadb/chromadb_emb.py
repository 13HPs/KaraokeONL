from chromadb.utils import embedding_functions

default_emb = embedding_functions.DefaultEmbeddingFunction()

name = "Custom Embedding Function"

emb = default_emb(name)

print(emb)