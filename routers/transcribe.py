from fastapi import APIRouter

router = APIRouter()


@router.post("/transcribe/", tags=["transcribe"])
async def transcribe():
    return [{"text": "transcribe"}, {"text": "transcribe"}]


