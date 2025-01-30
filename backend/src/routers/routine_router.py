from fastapi import APIRouter

router = APIRouter()

@router.post("/generate")
def generate_routine():
    return {"message": "Workout routine generated"}

@router.get("/list")
def list_routines():
    return {"message": "List all available workout routines"}

@router.post("/select")
def select_routine():
    return {"message": "Workout routine selected"}
