````markdown
# PDF RAG Chatbot

A Retrieval-Augmented Generation (RAG) based PDF Question Answering application that enables users to upload PDF documents and ask natural language questions about their content. The application extracts text from uploaded PDFs, generates semantic embeddings, stores them in a vector database, retrieves the most relevant context for each query, and generates accurate responses using a Large Language Model (LLM).

The project is built using **FastAPI**, **Express.js**, **LangChain**, **Voyage AI**, **Qdrant Cloud**, and **Groq Llama 3.3**.

---

# Features

- Upload PDF documents for question answering
- Retrieval-Augmented Generation (RAG) pipeline
- Semantic search using vector embeddings
- Automatic PDF parsing and chunking
- Voyage AI embeddings for document representation
- Qdrant Cloud vector database integration
- Groq Llama 3.3 model for response generation
- FastAPI backend for AI services
- Express.js frontend with EJS templates
- Modular backend architecture
- Secure environment variable configuration

---

# System Architecture

```
                        User
                          │
                          ▼
                Express.js Frontend
                          │
                          ▼
                    FastAPI Backend
                          │
          ┌───────────────┴───────────────┐
          │                               │
          ▼                               ▼
     PDF Upload                    User Question
          │                               │
          └───────────────┬───────────────┘
                          ▼
                    PyPDFLoader
                          │
                          ▼
        RecursiveCharacterTextSplitter
                          │
                          ▼
               Voyage AI Embeddings
                          │
                          ▼
             Qdrant Cloud Vector Store
                          │
                          ▼
          Similarity Search (Top-K Chunks)
                          │
                          ▼
               Retrieved Context Chunks
                          │
                          ▼
            Groq Llama 3.3 Large Language Model
                          │
                          ▼
                  AI Generated Response
                          │
                          ▼
                        User
```

---

# Technology Stack

## Frontend

- Express.js
- EJS
- HTML
- CSS
- Axios
- Multer

## Backend

- FastAPI
- Python
- LangChain

## AI and Machine Learning

- Groq Llama 3.3-70B Versatile
- Voyage AI Embeddings

## Vector Database

- Qdrant Cloud

## PDF Processing

- PyPDFLoader
- RecursiveCharacterTextSplitter

## Deployment (Planned)

- Docker
- Railway / Render
- Vercel

---

# Project Structure

```
Hello_pdf_chatter
│
├── ai_service
│   ├── chain
│   │   └── rag.py
│   │
│   ├── config
│   │   └── credentials.py
│   │
│   ├── embeddings
│   │   └── embedding_service.py
│   │
│   ├── loaders
│   │   └── pdf_loaders.py
│   │
│   ├── service
│   │   └── langchainService.py
│   │
│   ├── vectorStore
│   │   └── qdrant.py
│   │
│   ├── main.py
│   └── requirements.txt
│
├── config
│   └── db.js
│
├── database
│   └── createUserTable.js
│
├── views
│   ├── login.ejs
│   ├── signin.ejs
│   └── chatter.ejs
│
├── app.js
├── package.json
├── package-lock.json
└── .gitignore
```

---

# Installation

## Clone the Repository

```bash
git clone https://github.com/<your-github-username>/<repository-name>.git

cd <repository-name>
```

---

## Install Frontend Dependencies

```bash
npm install
```

---

## Install Backend Dependencies

```bash
cd ai_service

pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file inside the backend directory.

```env
VOYAGE_API_KEY=YOUR_VOYAGE_API_KEY

QDRANT_URL=YOUR_QDRANT_URL

QDRANT_API_KEY=YOUR_QDRANT_API_KEY

GROQ_API_KEY=YOUR_GROQ_API_KEY
```

---

# Running the Application

## Start the FastAPI Backend

```bash
cd ai_service

uvicorn main:app --reload
```

Backend URL:

```
http://127.0.0.1:8000
```

---

## Start the Express Frontend

```bash
npm start
```

or

```bash
node app.js
```

Frontend URL:

```
http://localhost:3000
```

---

# Application Workflow

1. The user uploads a PDF document.
2. The backend stores the uploaded file temporarily.
3. PyPDFLoader extracts the document content.
4. The extracted text is divided into overlapping chunks.
5. Voyage AI generates vector embeddings for each chunk.
6. The embeddings are stored in Qdrant Cloud.
7. The user submits a question.
8. A similarity search retrieves the most relevant document chunks.
9. The retrieved context and user question are sent to the Groq LLM.
10. The LLM generates a context-aware response.
11. The generated answer is returned to the frontend.

---

# Retrieval-Augmented Generation Pipeline

```
                 User Question
                       │
                       ▼
                Similarity Search
                       │
                       ▼
           Retrieve Relevant Chunks
                       │
                       ▼
                 Build Context
                       │
                       ▼
               Groq Llama 3.3
                       │
                       ▼
             Context-Aware Response
```

Instead of relying solely on the model's pre-trained knowledge, the application retrieves relevant information from the uploaded document before generating a response. This significantly improves answer accuracy and minimizes hallucinations.

---

# APIs and Services

| Service | Purpose |
|----------|---------|
| Voyage AI | Embedding Generation |
| Qdrant Cloud | Vector Database |
| Groq | Large Language Model |

---

# Core Concepts

- Retrieval-Augmented Generation (RAG)
- Semantic Search
- Vector Embeddings
- Prompt Engineering
- Similarity Search
- Vector Databases
- LangChain
- REST APIs
- FastAPI
- Express.js
- PDF Parsing
- Text Chunking

---

# Screenshots

## Login Page

_Add login page screenshot here._

---

## PDF Upload Interface

_Add upload page screenshot here._

---

## Chat Interface

_Add chatbot interface screenshot here._

---

## Generated Response

_Add generated response screenshot here._

---

# Future Enhancements

The following features are planned for future versions:

- Google OAuth Authentication
- JWT-based User Authentication
- Persistent User Sessions
- Multi-turn Conversations
- Chat History
- Upload Once and Ask Unlimited Questions
- Multiple PDF Management
- Source Citations with Page Numbers
- Conversation Memory
- Streaming Responses
- PostgreSQL Integration
- Docker Containerization
- Cloud Deployment
- Responsive User Interface
- Dark Mode
- PDF Preview
- Export Chat History
- Hybrid Search
- Re-ranking Pipeline
- Redis Caching

---

# Learning Outcomes

This project demonstrates practical implementation of:

- Retrieval-Augmented Generation (RAG)
- Large Language Model Integration
- LangChain Framework
- FastAPI Development
- Express.js Backend Development
- Vector Database Integration
- Semantic Search
- Prompt Engineering
- REST API Communication
- PDF Processing
- Modular Software Architecture

---

# Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a new branch.

```bash
git checkout -b feature-name
```

3. Commit your changes.

```bash
git commit -m "Add feature"
```

4. Push your branch.

```bash
git push origin feature-name
```

5. Open a Pull Request.

---

# License

This project is intended for educational and learning purposes.

---

# Author

**Priya Kumari**

B.Tech, Electronics and Communication Engineering  
National Institute of Technology, Jamshedpur

**GitHub:** https://github.com/<your-github-username>

**LinkedIn:** https://www.linkedin.com/in/<your-linkedin-profile>
````
