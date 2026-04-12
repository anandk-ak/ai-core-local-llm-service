from fastapi import APIRouter
from app.services.llm_service import generate_text

router = APIRouter()

@router.post("/generate")
def generate(request: dict):
    response = generate_text(request["prompt"], request.get("model", "mistral"))
    return {"response": response}
