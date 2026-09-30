# Real Estate AI Assistant

A Retrieval-Augmented Generation (RAG) based AI assistant that retrieves information from provided web articles and uses an LLM to answer questions based on the retrieved content.

## Project Overview

The Real Estate AI Assistant allows users to:

* Provide one or more website URLs
* Extract content from the provided webpages
* Split the content into smaller chunks
* Convert chunks into vector embeddings
* Store embeddings in ChromaDB
* Retrieve relevant information for a user's question
* Generate an answer using an LLM
* Display the source URLs used for the answer

## How It Works

```text
Website URLs
     ↓
Web Scraping
     ↓
Text Extraction
     ↓
Text Splitting
     ↓
Hugging Face Embeddings
     ↓
ChromaDB Vector Store
     ↓
Similarity Search
     ↓
Relevant Documents
     ↓
Groq LLM
     ↓
Answer + Sources
```

## Technologies Used

* Python
* Streamlit
* LangChain
* ChromaDB
* Hugging Face Embeddings
* Groq LLM
* RAG (Retrieval-Augmented Generation)

## Embedding Model

The project uses:

`thenlper/gte-small`

It converts the extracted text into numerical vector representations that can be stored and searched in ChromaDB.

## Features

* URL-based knowledge retrieval
* Semantic search using vector embeddings
* Question answering using retrieved context
* Source-aware responses
* Streamlit web interface
* Multiple URL support
* Persistent ChromaDB vector storage

## Project Structure

```text
real_estate_ai_assistant/
│
├── main.py
├── rag.py
├── prompt.py
├── requirements.txt
│
├── resources/
│   └── vectorstore/
│
└── screenshots/
    └── project.png
```

## Installation

Clone the repository:

```bash
git clone https://github.com/rschaurasiya/Real_Estate_AI_Assistant.git
cd Real_Estate_AI_Assistant
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Create a `.env` file and add your Groq API key:

```text
GROQ_API_KEY=your_api_key
```

## Run the Application

Start the Streamlit application:

```bash
streamlit run main.py
```

Then open the local Streamlit URL shown in the terminal.

## Example

Provide a news/article URL, such as an article related to the housing market or mortgage rates.

Then ask questions such as:

* What happened to home sales?
* Why did mortgage rates change?
* How does the Federal Reserve affect mortgage rates?
* What factors affected the housing market?

The assistant retrieves relevant information from the provided webpages and generates an answer based on that information.

## Project Screenshot

![Real Estate AI Assistant](screenshots/project.png)
![Real Estate AI Assistant](screenshots/project_1.png)

## Key Learning

This project demonstrates how RAG can connect an LLM with external information sources instead of relying only on the model's existing knowledge.

The project covers the complete flow:

**Web Data → Embeddings → Vector Database → Retrieval → LLM → Answer**

## Author

**Radheshyam Kumar Chaurasiya**

B.Tech Computer Science & Engineering Student
Interested in Data Science, Machine Learning, LLMs and Agentic AI.
