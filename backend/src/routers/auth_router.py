from fastapi import APIRouter

router = APIRouter()

@router.post("/login")
def login():
    return {"message": "User logged in successfully"}

@router.post("/logout")
def logout():
    return {"message": "User logged out successfully"}

@router.get("/user")
def get_user():
    return {"message": "Fetch user profile"}
