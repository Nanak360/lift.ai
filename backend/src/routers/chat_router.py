from fastapi import APIRouter

router = APIRouter()

@router.post("/message")
def chat_with_llm():
    return {"message": "Chat response from LLM"}
