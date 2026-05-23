# Policy RAG Chatbot

## Project Overview
This project is a Retrieval-Augmented Generation (RAG) chatbot built with Flask, ChromaDB, and Sentence Transformers.

The chatbot allows users to ask questions about company policies and retrieves the most relevant policy document before generating an answer.

---

## Features
- Policy document retrieval
- Semantic search using embeddings
- Flask web application
- Interactive UI
- Source citation display
- ChromaDB vector database

---

## Technologies Used
- Python
- Flask
- Sentence Transformers
- ChromaDB
- HTML/CSS/JavaScript

---

## Project Structure

```text
rag-policy-chatbot/
│
├── app.py
├── requirements.txt
├── README.md
├── ai-tooling.md
├── design-and-evaluation.md
│
├── policies/
│   ├── pto.txt
│   ├── remote-work.txt
│   ├── security.txt
│   └── expenses.txt
│
└── venv/