from fastapi import APIRouter

router = APIRouter()

@router.post("/save")
def save_embedding():
    return {"message": "Embedding saved successfully"}

@router.get("/search")
def search_embedding():
    return {"message": "Retrieve relevant embeddings"}
