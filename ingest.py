import os
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from vector_store import save_vector_store

DATA_DIR = "data_sources"

def simple_split(text, chunk_size=500):
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i+chunk_size])
    return chunks

def ingest():
    all_text = ""

    for file in os.listdir(DATA_DIR):
        if file.endswith(".txt"):
            docs = TextLoader(os.path.join(DATA_DIR, file)).load()
            for d in docs:
                all_text += d.page_content + "\n"

    text_chunks = simple_split(all_text)

    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    db = FAISS.from_texts(text_chunks, embeddings)
    save_vector_store(db)
