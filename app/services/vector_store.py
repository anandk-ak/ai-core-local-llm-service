import chromadb
from sentence_transformers import SentenceTransformer

# Initialize embedding model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Initialize Chroma: Persist it since we saw data loss without this
client = chromadb.PersistentClient(path="./chroma_db")

#client = chromadb.Client(
#    chromadb.config.Settings(
#        persist_directory="./chroma_db"
#    )
#)

def get_collection(name: str):
    return client.get_or_create_collection(name=name)

def add_documents(collection_name: str, documents: list[str]):
    collection = get_collection(collection_name)

    embeddings = embedding_model.encode(documents).tolist()

    ids = [f"id_{i}" for i in range(len(documents))]

    collection.add(
        documents=documents,
        embeddings=embeddings,
        ids=ids
    )
    # client.persist()
