from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from fastapi import UploadFile

from embeddings.process_pdf import extract_text_from_pdf
from embeddings.vector_db import store_vectors, retrieve_embedding
from utils.save_and_get_file_url import save_and_get_file_path

router = APIRouter()

class EmbeddingRequest(BaseModel):
    source_type: str
    files: UploadFile

@router.post("/save")
async def save_embeddings(files: list[UploadFile]):
    """Extract text and save embeddings"""
    try:
        all_docs = []
        for file in files:
            path = save_and_get_file_path(file)
            all_docs.extend(await extract_text_from_pdf(path))
        store_vectors(all_docs)
        return {"message": "Embedding saved successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

@router.get("/search")
def search_embeddings(query: str):
    """Search for relevant embeddings"""
    try:
        return {"results": retrieve_embedding(query)}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
