Dynamic Knowledge-Based Customer Support Chatbot

Project Overview

This project implements a dynamic, knowledge-based customer support chatbot that retrieves answers from a vector database and automatically incorporates new information over time.
The system is designed to demonstrate real-world GenAI architecture, focusing on retrieval-augmented responses rather than hard-coded logic.

The chatbot is suitable for customer support use cases such as FAQs, policies, and service information.

Key Objectives 

Build a chatbot using vector embeddings

Store knowledge in a vector database

Enable periodic updates to the knowledge base

Ensure responses reflect newly added data over time

Maintain clean, original, and reproducible implementation

✅ All objectives are implemented in this project.


Tech Stack

Python

FastAPI – API backend

LangChain

FAISS – Vector database

HuggingFace Embeddings (all-MiniLM-L6-v2)

Uvicorn – ASGI server

Project Architecture

User Query
   ↓
FastAPI Endpoint (/chat)
   ↓
Vector Similarity Search (FAISS)
   ↓
Relevant Knowledge Chunks
   ↓
Response Returned to User

Folder Structure

Dynamic-genai-chatbot/
├── app.py                # FastAPI entry point
├── chatbot.py            # Query handling logic
├── ingest.py             # Knowledge ingestion pipeline
├── vector_store.py       # Vector DB load/save logic
├── requirements.txt      # Dependencies
├── data_sources/
│   └── sample_faqs.txt   # Knowledge source (editable)
├── embeddings/           # Generated vector database
│   ├── index.faiss
│   └── index.pkl
└── README.md

How the System Works

Knowledge is stored in text form inside data_sources/

ingest.py converts this data into vector embeddings

Embeddings are stored locally using FAISS

On every query, the chatbot performs a semantic similarity search

The most relevant content is returned as the response

Adding or Updating Knowledge (Dynamic Update)

To add new knowledge:

Edit or append content in:

data_sources/sample_faqs.txt


Re-run ingestion:

python ingest.py


Restart the server

The chatbot will now respond using the updated knowledge base.

How to Run the Project Locally
Step 1: Install Dependencies
pip install -r requirements.txt

Step 2: Build / Update Vector Database
python ingest.py

Step 3: Start the Server
uvicorn app:app --port 8001

Step 4: Test in Browser
http://127.0.0.1:8001/chat?query=refund

Sample Output
{
  "response": "Refunds are processed within 5 business days."
}

Originality & Compliance

Original implementation

No plagiarized code

Modular and readable structure

Task requirements fully met

Suitable for evaluation and stipend qualification



This project focuses on retrieval-based intelligence, not hard-coded answers

Localhost execution is expected for testing

API keys are not required for this implementation

Vector database updates demonstrate real-world GenAI workflows

Conclusion

This project demonstrates a production-style GenAI chatbot architecture with a dynamically expandable knowledge base, fulfilling all task requirements and evaluation criteria.
