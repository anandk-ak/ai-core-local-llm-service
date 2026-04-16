PROJECT: AI Core + RAG Platform

SETUP:
- FastAPI backend
- Ollama running locally (model: mistral)
- ChromaDB (PersistentClient, local storage)
- Sentence Transformers for embeddings

ARCHITECTURE:
- API → RAG layer → LLM → Response
- Collection-based routing for different knowledge domains

ENDPOINTS:
- POST /generate → accepts:
  {
    "prompt": "...",
    "model": "mistral",
    "collection": "optional"
  }
- GET /health

RAG STATUS:
- Vector DB implemented using ChromaDB
- Persistent storage enabled (./chroma_db)
- Retrieval working (top-k context injected into prompt)
- Collections supported (e.g., "laptop_metrics")

CURRENT CAPABILITIES:
- LLM responses via Ollama
- Context-aware responses using RAG
- Logging enabled (request + response + retrieval)

PROJECT GOAL:
- Build AI-powered laptop monitoring system
- Analyze CPU, memory, disk metrics
- Provide insights + recommendations

NEXT STEP:
- Ingest real laptop metrics (psutil)
- Feed into AI Core for analysis

ASK:
Continue from this state and guide next implementation steps.
