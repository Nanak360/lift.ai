from fastapi import APIRouter

router = APIRouter()

@router.post("/log")
def log_workout():
    return {"message": "Workout logged successfully"}

@router.get("/progress")
def get_progress():
    return {"message": "Fetch workout progress"}
