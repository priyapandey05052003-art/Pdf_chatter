from fastapi import FastAPI, UploadFile, File, Form, HTTPException

from service.langchainService import (
    load_pdf,
    create_vector_db,
    retrieve_chunks,
    generate_answer,
)

app = FastAPI()

@app.post("/ask")
async def ask_question(
    pdf: UploadFile = File(...),
    question: str = Form(...),
):
    try:

        # Load and split the PDF
        chunks, collection_name = await load_pdf(pdf)

        # Create the vector store
        vector_store = create_vector_db(
            chunks,
            collection_name,
        )

        if vector_store is None:
            raise HTTPException(
                status_code=500,
                detail="Failed to create vector store.",
            )

        # Retrieve relevant chunks
        retrieved_docs = retrieve_chunks(
            vector_store,
            question,
        )

        # Generate answer using Groq
        answer = generate_answer(
            question,
            retrieved_docs,
        )

        return {
            "answer": answer,
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e),
        )
        
        