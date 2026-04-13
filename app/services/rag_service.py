from app.services.vector_store import get_collection, embedding_model

def retrieve_context(collection_name: str, query: str) -> str:
    collection = get_collection(collection_name)

    query_embedding = embedding_model.encode([query]).tolist()

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=3
    )

    documents = results.get("documents", [])

    if documents and len(documents) > 0:
        return "\n".join(documents[0])

    return ""
