# Policy RAG Chatbot

## Overview

This project is a lightweight Retrieval-Augmented Generation (RAG) chatbot that answers employee policy questions using company policy documents.

The chatbot retrieves relevant information from policy files and provides answers with source citations.

## Features

- Policy question answering
- Source citation display
- Multi-document retrieval
- Web interface
- Public deployment on Render
- GitHub Actions CI/CD

## Architecture

User Question
↓
TF-IDF Vectorizer
↓
Cosine Similarity Search
↓
Top Matching Policy Documents
↓
Answer + Source Citations

## Policy Documents

- PTO Policy
- Remote Work Policy
- Security Policy
- Expense Policy
- Holiday Policy
- Code of Conduct Policy
- Travel Policy
- Data Privacy Policy

## Installation

```bash
pip install -r requirements.txt
python app.py