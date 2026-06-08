# Design and Evaluation

## Design Choices

### Retrieval Method

Initially, Sentence Transformers and ChromaDB were used.

However, deployment on Render Free Tier exceeded the 512MB memory limit.

To improve deployment reliability, the project was redesigned using:

- TF-IDF Vectorizer
- Cosine Similarity Search

This approach reduced memory consumption significantly while maintaining retrieval quality.

## Architecture

1. Load policy documents
2. Create TF-IDF vectors
3. Receive user question
4. Calculate cosine similarity
5. Retrieve top matching documents
6. Return answer with source citations

## Evaluation Metrics

### Groundedness

Answers are generated only from policy documents.

Result: Excellent

### Citation Accuracy

Sources are displayed below every answer.

Result: Excellent

### Latency

Average response time:

- Local: < 1 second
- Render: 1-3 seconds

Result: Excellent

## Deployment

Platform: Render

Status: Successfully deployed

## CI/CD

Platform: GitHub Actions

Status: Successfully running on push

## Conclusion

The system successfully retrieves relevant policy information, provides citations, and operates within Render's memory constraints.