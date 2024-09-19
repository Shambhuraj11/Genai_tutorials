# RAG Tutorials Files

## What is RAG?
RAG is Retrieval angumented generation, it is a technique that enhances language model generation by incorporating external knowledge.This typically done by retrieving relevent information from a large corpus of documents to answer particular question.

or 

With RAG, LLM can able to leverage knowledge and information this is not necessarily in its weight means not a part of its training data.

## Why should use RAG?
- limited knowledge access
- Lack of transparency : LLM struggles to provide transparent or relevant information
- Hallucination in answers.

## RAG Architecture

### Ingestion

A. Document:

   - A typical RAG pipeline have knowledge source like local files, CSV, TSV, txt, pdf, json, web pages, cloud files.

B. Chunking 
   
   - Here we split data into chunks.

   - It ensure model is not overloaded by too much information and help to keep input under input context limit of model.

   - Too small size of chunk will won't provide you information enough to answer question and Too large size of chunk will introduce noise and reducing the retrieval accuracy

   - Data Characterstics, Retriever constraints, memory and computational resources, Task requirement, experimentation, Overlap Consideration are factor can help to decide ideal chunk size.

   - https://www.pinecone.io/learn/chunking-strategies/

C. Embedding
   
   - Vector embedding is numerical representation of text data.

   - Frequency based embeddings: TF-IDF, N-Grams, Neural Network based embeddings: Word2Vec, Bert, Elmo

   - Sentence transformers is typically optimized for producing numerical representation at sentence level, also capturing the overall semantics of sentences.

D. Vector Embedding indexing
   
   - Vector index is data structure used to efficiently store and retrieve high dimensional vector data, enabling fast similarity search and nearest neighbour queries.
   
