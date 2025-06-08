from fastapi import FastAPI

from routers import transcribe_router

app = FastAPI()

app.include_router(transcribe_router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Hello SympTalk Service!"}
