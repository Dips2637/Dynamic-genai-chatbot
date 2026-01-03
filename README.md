Dynamic Knowledge-Based Customer Support Chatbot

Project Overview

This project implements a dynamic customer support chatbot that retrieves intelligent answers from a continuously updatable knowledge base using a vector database.
The system is designed to automatically incorporate new information over time without changing application code, fulfilling the requirements of a real-world GenAI-style support system.

The chatbot uses semantic similarity search over vector embeddings to respond to user queries in real time.

Problem Statement

Traditional chatbots rely on static, hard-coded responses, which makes them difficult to maintain and update.
This project solves that problem by:

Separating knowledge from code

Using a vector database for semantic retrieval

Allowing the knowledge base to expand dynamically over time

Key Features

📦 Dynamic Knowledge Base (external text files)

🔍 Vector Database (FAISS) for semantic search

🔁 Automatic knowledge ingestion

⚡ Real-time API responses

🧩 Modular, original implementation

🧪 Fully local, no paid APIs required

System Architecture
User Query
    ↓
FastAPI Endpoint (/chat)
    ↓
Vector Database (FAISS)
    ↓
Semantic Similarity Search
    ↓
Relevant Knowledge Retrieved
    ↓
Response Returned to User


This follows a retrieval-augmented architecture, commonly used in GenAI systems.

Technology Stack
Component	Technology
Backend API	FastAPI
Vector Database	FAISS
Embeddings	Sentence-Transformers
Language	Python
Deployment	Local (Uvicorn)
Project Structure


dynamic-genai-chatbot/
│
├── app.py                  # FastAPI application
├── ingest.py               # Knowledge ingestion logic
├── chatbot.py              # Query handling logic
├── vector_store.py         # Vector DB operations
├── requirements.txt
│
├── data_sources/
│   └── sample_faqs.txt     # Knowledge base (editable)
│
└── embeddings/             # Vector database (generated at runtime)



How Dynamic Knowledge Expansion Works

Knowledge is stored in external text files inside data_sources/.

At application startup, the system:

Reads all files

Converts text into vector embeddings

Stores them in a FAISS vector database

When a user asks a question:

The query is embedded

Semantic similarity search is performed

The most relevant knowledge is returned

➕ Adding New Knowledge (No Code Change)

Open data_sources/sample_faqs.txt

Add new information, for example:

Office hours are Monday to Friday, 9 AM to 6 PM.


Save the file

Restart the server

The chatbot will automatically start answering questions using the new knowledge.

Setup & Execution
Install Dependencies
pip install -r requirements.txt

Run the Application
uvicorn app:app --port 8001

Test the Chatbot

Open browser:

http://127.0.0.1:8001/chat?query=refund

Originality & Compliance Declaration

This project is independently developed as part of an internship task.

No external repositories or copied implementations were used.

Only open-source libraries were utilized.

The solution is original, plagiarism-free, and fully compliant with conduct guidelines.

Conclusion

This project demonstrates a practical, scalable approach to building an intelligent customer support chatbot using vector databases and semantic retrieval.
The architecture is LLM-ready and can be extended with generative models if required in the future.