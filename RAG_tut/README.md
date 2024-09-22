# RAG Tutorials Files

## What is RAG?

Retrieval-Augmented Generation (RAG) is a technique that enhances language model outputs by incorporating external knowledge. It achieves this by retrieving relevant information from a large corpus of documents to answer a specific query.

Alternatively,

RAG enables Large Language Models (LLMs) to leverage knowledge and information that is not embedded within their model weights, meaning it can access information beyond its training data.

## Why should use RAG?
- Limited Knowledge Access: LLMs have a fixed knowledge base tied to their training data, which may become outdated or incomplete over time.
- Lack of Transparency: LLMs often struggle to provide clear, relevant information or justify their responses.
- Hallucinations: LLMs may generate incorrect or fabricated answers, known as hallucinations. RAG helps mitigate this by grounding responses in external data.

## RAG Architecture

### Ingestion

#### A. Document Sources:
   A typical RAG pipeline incorporates knowledge from sources such as:
      - Local files (CSV, TSV, TXT)
      - PDFs
      - JSON files
      - Web pages
      - Cloud-based documents

#### B. Chunking:
      - The document data is split into smaller, manageable chunks.
      - Chunking ensures that the model isn’t overwhelmed with too much information, keeping the input    within the context limit of the model.
      - An ideal chunk size balances the need for context. Chunks that are too small may lack sufficient information to answer a query, while chunks that are too large may introduce noise, reducing retrieval accuracy.
      - Factors influencing chunk size include data characteristics, retriever constraints, available memory, computational resources, task requirements, and overlap considerations.

#### C. Embedding:
     - Embeddings are numerical representations of text data.
     - Examples include frequency-based embeddings like TF-IDF and n-grams, as well as neural network-based embeddings like Word2Vec, BERT, and ELMo.
     - Sentence transformers are typically used to generate embeddings at the sentence level, capturing the overall meaning of a sentence.

#### D. Vector Embedding Indexing:
     - Vector indices are data structures designed to efficiently store and retrieve high-dimensional vector data, enabling fast similarity search and nearest-neighbour queries.

### Retrieval Processes

#### A. Standard Naive Approach:
   Works well with small, manageable chunks of data.

#### B. Sentence-Window Retrieval:
    - Retrieves the sentence most relevant to the user’s query using similarity search.
    - A static sentence window is applied to retrieve surrounding context, thus improving the quality of the response.

#### C. Auto-Merging / Hierarchical Retrieval:
    - Combines information from multiple sources to provide a more comprehensive answer.
    - Particularly useful when a single corpus doesn't fully answer a query, but combining data from multiple sources can.
    - However, this method can be computationally intensive and prone to overgeneralization.

#### D. Ensemble Retrieval and Re-Ranking:
    - The user’s query is passed across multiple retrievers, and the results are aggregated.
    - Ensemble Retriever combines results from different retrieval methods.
    - EnsembleRetriever re-ranks the results using algorithms like Reciprocal Rank Fusion, enhancing the accuracy and relevance of the final answer.
