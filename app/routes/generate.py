from pydantic import BaseModel
from fastapi import APIRouter
from app.services.llm_service import generate_text

router = APIRouter()

class GenerateRequest(BaseModel):
    prompt: str
    model: str = "mistral"   # default


@router.post("/generate")
def generate(request: GenerateRequest):
    response = generate_text(request.prompt, request.model)
    return {"response": response}
