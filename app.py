from fastapi import FastAPI
from ingest import ingest
from chatbot import ask_bot

app = FastAPI()

ingest()

@app.get("/chat")
def chat(query: str):
    return {"response": ask_bot(query)}
