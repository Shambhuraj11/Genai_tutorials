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
   
### Retrieval Processes

   A. Standard naive approach: 
      
      - This works well with small chunks. 

   B. Sentence-window retrieval 
     
      - During retrieval, we retrieve the sentence that are most relevant to user query via similarity search and replace the sentence with full surrounding context (Using static-sentence-window around the context, implemented by retrieving sentences surrounding the one being originally retrieved)

   C. Auto-merging/ Hierarchical  Retriever

      - This aims to combine information from multiple resources. This method is useful when single corpus do not fully answer the user query rather answer lies in combining information from multiple resources.
      - chances of overgeneralization and Computationally heavy

   D. Ensemble Retrieval and Re-Ranking

      - This method involves passing usery query across different retrievers. Ensemble retriever ensemble results from different retrievers. EnsembleRetriever rerank the results of constituent retriever based on reciprocal rank fusion algorithm
      
       

   