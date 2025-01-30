# FastAPI Entry Point
from fastapi import FastAPI
from routers.auth_router import router as auth_router
from routers.embeddings_router import router as embeddings_router
from routers.user_router import router as user_router
from routers.routine_router import router as routine_router
from routers.tracking_router import router as tracking_router
from routers.chat_router import router as chat_router

app = FastAPI()

# Include Routers
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(embeddings_router, prefix="/embeddings", tags=["Embeddings"])
app.include_router(user_router, prefix="/user", tags=["User Profile"])
app.include_router(routine_router, prefix="/routine", tags=["Workout Routines"])
app.include_router(tracking_router, prefix="/tracking", tags=["Workout Tracking"])
app.include_router(chat_router, prefix="/chat", tags=["LLM Chat"])

@app.get("/")
def root():
    return {"message": "Welcome to the Bodybuilding LLM API!"}
