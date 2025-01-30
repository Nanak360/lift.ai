from fastapi import APIRouter

router = APIRouter()

@router.post("/profile")
def save_user_profile():
    return {"message": "User profile saved successfully"}

@router.get("/profile")
def get_user_profile():
    return {"message": "Fetch user profile"}

@router.get("/questions")
def ask_user_questions():
    return {"message": "Ask user personalized questions"}
