from pydantic import BaseModel
from fastapi import APIRouter
from app.services.llm_service import generate_text
from typing import Optional

router = APIRouter()

class GenerateRequest(BaseModel):
    prompt: str
    model: str = "mistral"   # default
    collection: Optional[str] = None


@router.post("/generate")
def generate(request: GenerateRequest):
    response = generate_text(request.prompt, request.model, request.collection)
    return {"response": response}
