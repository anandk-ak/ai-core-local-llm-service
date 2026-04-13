from fastapi import FastAPI
from app.routes import generate
import requests

app = FastAPI(title="AI Core Service")

app.include_router(generate.router)


@app.get("/health")
def health():
    try:
        res = requests.get("http://localhost:11434")
        if res.status_code == 200:
            return {"status": "ok", "ollama": "running"}
        else:
            return {"status": "degraded", "ollama": "not responding"}
    except Exception:
        return {"status": "down", "ollama": "not reachable"}
