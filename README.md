# Incident Management RAG Assistant

## Overview

Incident Management RAG Assistant is a Retrieval-Augmented Generation (RAG) application that enables users to query incident management reports using natural language.

The application ingests PDF-based incident reports, stores document embeddings in Qdrant, retrieves relevant incident information using semantic search, and generates context-aware answers using Gemini 2.5 Flash.

---

## Features

* PDF ingestion and document chunking
* Semantic search using HuggingFace embeddings
* Qdrant Vector Database integration
* Max Marginal Relevance (MMR) retrieval
* Gemini 2.5 Flash powered answer generation
* Pydantic structured output validation
* Page-level source attribution
* Dockerized Qdrant deployment

---

## Architecture

PDF Documents
↓
Chunking
↓
Embeddings (BAAI/bge-base-en-v1.5)
↓
Qdrant Vector Database
↓
Retriever (MMR)
↓
Gemini 2.5 Flash
↓
Pydantic Structured Output

---

## Tech Stack

* Python
* LangChain
* Qdrant
* HuggingFace Embeddings
* Gemini 2.5 Flash
* Pydantic
* Docker

---

## Installation

### Clone Repository

git clone <repository-url>

cd incident-management-rag

### Install Dependencies

pip install -r requirements.txt

### Configure Environment Variables

Create a .env file:

GEMINI_API_KEY=your_api_key

QDRANT_URL=http://localhost:6333

---

## Start Qdrant

docker compose up -d

---

## Index Documents

python indexing.py

---

## Run Application

python rag_pipeline.py

---

## Sample Questions

* What is the root cause of INC-0100?
* Tell me about INC-0050.
* What issues occurred in the API Gateway service?
* Which incidents have severity P1?
* What prevention actions were taken for INC-0020?

---

## Future Enhancements

* Streamlit Frontend
* Hybrid Search (Vector + Keyword)
* Conversation Memory
* LangGraph Agent Integration
* Source Citations and Confidence Scores

---

## Author
Anirudh Bhardwaj
