# Design and Evaluation

## Design Choices

### Embedding Model
The project uses the Sentence Transformers model:
all-MiniLM-L6-v2

This model was selected because it is lightweight, fast, and effective for semantic similarity search.

### Vector Database
ChromaDB was used as the vector database because it is lightweight, easy to use locally, and integrates well with Python.

### Architecture
The system architecture includes:

1. Policy text documents
2. Sentence-transformer embeddings
3. ChromaDB vector storage
4. Flask web application
5. REST API endpoints

### Retrieval Process
The application converts user questions into embeddings and retrieves the most relevant policy document from ChromaDB.

### Prompting Strategy
The retrieved document text is returned directly as the answer together with the document source citation.

## Evaluation

### Evaluation Questions

The chatbot was tested using questions related to:
- PTO policy
- Remote work
- Security policy
- Expense reimbursement

### Groundedness
The chatbot responses were grounded in the stored policy documents.

### Citation Accuracy
The chatbot correctly returned the source policy file for responses.

### Latency
Average response time was under 2 seconds on local execution.

## Future Improvements

- Add OpenAI or Groq LLM generation
- Add multi-document retrieval
- Add PDF ingestion
- Add better UI styling
- Add deployment to Render or Railway