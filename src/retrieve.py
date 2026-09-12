"""
Thin retrieval layer over the Chroma collection built by ingest.py.
"""
import os
import chromadb
from chromadb.utils import embedding_functions

DB_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "vectorstore")
COLLECTION_NAME = "rulebook"
EMBED_MODEL = "all-MiniLM-L6-v2"

_client = None
_collection = None


def get_collection():
    global _client, _collection
    if _collection is None:
        _client = chromadb.PersistentClient(path=DB_DIR)
        embed_fn = embedding_functions.SentenceTransformerEmbeddingFunction(model_name=EMBED_MODEL)
        _collection = _client.get_collection(name=COLLECTION_NAME, embedding_function=embed_fn)
    return _collection


def retrieve(query, k=6):
    """
    Returns a list of dicts: {id, text, source_file, section, distance}
    sorted by relevance (lowest distance first).
    """
    collection = get_collection()
    results = collection.query(query_texts=[query], n_results=k)

    out = []
    ids = results["ids"][0]
    docs = results["documents"][0]
    metas = results["metadatas"][0]
    dists = results["distances"][0]
    for i in range(len(ids)):
        out.append({
            "id": ids[i],
            "text": docs[i],
            "source_file": metas[i].get("source_file"),
            "section": metas[i].get("section"),
            "distance": dists[i],
        })
    return out
