from vector_store import load_vector_store

def ask_bot(query: str):
    db = load_vector_store()
    docs = db.similarity_search(query, k=2)
    return docs[0].page_content
