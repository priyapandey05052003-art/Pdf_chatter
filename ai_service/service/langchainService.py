from pathlib import Path
import shutil
import re

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_voyageai import VoyageAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from langchain_groq import ChatGroq

from config.credentials import (
    VOYAGE_API_KEY,
    QDRANT_URL,
    QDRANT_API_KEY,
    GROQ_API_KEY,
)


# Embedding Model
embeddings = VoyageAIEmbeddings(
    model="voyage-4-lite",
    voyage_api_key=VOYAGE_API_KEY,
)

# LLM
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=GROQ_API_KEY,
)


async def load_pdf(uploaded_file):

    temp_dir = Path("temp")
    temp_dir.mkdir(exist_ok=True)

    pdf_path = temp_dir / uploaded_file.filename

    with open(pdf_path, "wb") as buffer:
        shutil.copyfileobj(uploaded_file.file, buffer)

    loader = PyPDFLoader(str(pdf_path))
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
    )

    chunks = splitter.split_documents(documents)

    collection_name = re.sub(
        r"[^a-zA-Z0-9_]",
        "_",
        pdf_path.stem.lower(),
    )

    return chunks, collection_name


def create_vector_db(chunks, collection_name):

    vector_store = QdrantVectorStore.from_documents(
        documents=chunks,
        embedding=embeddings,
        url=QDRANT_URL,
        api_key=QDRANT_API_KEY,
        collection_name=collection_name,
    )

    return vector_store


def retrieve_chunks(vector_store, question):

    results = vector_store.similarity_search(
        query=question,
        k=4,
    )

    return results


def generate_answer(question, retrieved_docs):

    context = "\n\n".join(
        doc.page_content
        for doc in retrieved_docs
    )

    prompt = f"""
You are a helpful AI assistant.

Answer the user's question using ONLY the context provided below.

If the answer cannot be found in the context, reply exactly:
"I couldn't find the answer in the uploaded document."

Context:
{context}

Question:
{question}

Answer:
"""

    print("Calling Groq...")

    response = llm.invoke(prompt)

    print("Groq responded.")

    return response.content

