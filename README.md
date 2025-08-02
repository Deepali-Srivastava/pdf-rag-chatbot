
# PDF RAG Chatbot

This project is a Retrieval-Augmented Generation (RAG) chatbot built with Python, LangChain, and OpenAI, designed for asking questions and getting concise answers from any PDF document.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Folder Structure](#folder-structure)
- [Setup Instructions](#setup-instructions)
- [How It Works](#how-it-works)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Customization](#customization)


## Overview

The HR Policy RAG chatbot lets users query an HR Policy Manual PDF. It uses embedding-based retrieval and a language model to provide concise answers based on the information in the manual.

## Features

- **PDF Processing**: Automatically loads and chunks PDF documents
- **Contextual Retrieval**: Finds the most relevant context for each question
- **Short Answers**: Answers are limited to 2–3 lines based on retrieved context
- **Interactive CLI**: Ask questions in a terminal prompt

## Folder Structure
```
pdf-rag-chatbot/
├── vectorstores/
│ └── hr_policy/
│ ├── index.faiss
│ └── index.pkl
├── venv/ # (Optional) your virtual environment
├── .env # Your environment variables file (not tracked)
├── HR_Policy_Manual.pdf # The PDF file with HR policies
├── query_processing.py # Script for interactive QA
├── requirements.txt # All Python dependencies
└── setup_vectorstore.py # Script for initial vectorstore setup (embedding & saving)
```


## Setup Instructions

1. **Clone the Repository:**

   ```
   git clone https://github.com/....../your-repo-name.git
   cd pdf-rag-chatbot
   ```
2. **(Optional) Create and activate a virtual environment:**

- For **Windows**:
  ```
  python -m venv venv
  venv\Scripts\activate
  ```
- For **macOS/Linux**:
  ```
  python3 -m venv venv
  source venv/bin/activate
  ```

  
  Creating a virtual environment is optional but recommended. It keeps project dependencies isolated from your system Python. The dependencies will be installed in     an isolated environment.


2. **Install Dependencies:**
   ```
   pip install -r requirements.txt
    ```


3. **Setup your `.env`:**

   Create a `.env` file in the root directory and include your OpenAI API key:
   ```
   OPENAI_API_KEY="your_openai_api_key"
    ```


4. **Place HR Policy PDF:**

   Place your `HR_Policy_Manual.pdf` in the root folder (replace or rename as necessary).

5. **Create the vectorstore directory:**

   Before running the vectorstore setup script, manually create the folder path for storing vectors:
   ```
   mkdir -p vectorstores/hr_policy
    ```
    **Note:** This folder is where the vector embeddings will be saved by `setup_vectorstore.py`.

6. **Generate the Vectorstore:**
   ```
   python setup_vectorstore.py
    ```

7. **Start Asking Questions:**
   ```
   python query_processing.py
   ```


## How It Works

- **setup_vectorstore.py**:  
Loads the HR Policy PDF, splits it into chunks, creates vector embeddings, and saves them for fast retrieval.

- **query_processing.py**:  
Loads the saved vectorstore and launches a loop where you can ask questions in the terminal. Retrieves context using semantic search, then uses a language model to generate a concise, context-constrained answer.

## Usage
 ```
python query_processing.py
 ```
Ask a question (or type 'exit' to quit): What is the company's leave policy?

Answer: [Model-generated answer based on manual, 2–3 lines]


## Dependencies

- langchain
- langchain-core
- langchain_community
- langchain-openai
- python-dotenv
- faiss-cpu
- pymupdf

Install all dependencies with:
```
pip install -r requirements.txt
```


## Customization

- To use a different PDF, replace `HR_Policy_Manual.pdf` and rerun `setup_vectorstore.py`.
- Change chunking or retriever parameters in the scripts for different document sizes or styles.
- Adjust language model settings as needed (see `query_processing.py`).

