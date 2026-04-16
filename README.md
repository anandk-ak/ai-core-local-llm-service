# ai-core-local-llm-service
Local-first AI Core API using Ollama + FastAPI for building reusable enterprise AI applications



Folder Structure: (We are moving into project wisse folders. laptop_monitor being a case in point

ai-core-local-llm-service/
│
├── app/                          # ✅ Your AI Core (DO NOT TOUCH MUCH)
│   ├── main.py
│   ├── routes/
│   └── services/
│
├── laptop_monitor/               # 🆕 Your project starts here
│   ├── __init__.py
│   │
│   ├── collector/                # 📊 Collect system metrics - psutil code (CPU, memory, disk
│   │   └── metrics_collector.py
│   │
│   ├── prompts/                  # 🧠 Prompt templates - Convert metrics → AI prompt
│   │   └── prompt_builder.py
│   │
│   ├── client/                   # 🔗 Calls AI Core API - Call your /generate API
│   │   └── ai_client.py
│   │
│   ├── runner/                   # ▶️ Entry point - Main script to run everything
│   │   └── run_monitor.py
│   │
│   └── storage/                  # 💾 (future) store history - (Later) save metrics history
│       └── metrics_store.py
│
├── chroma_db/                    # ✅ Vector DB (auto-created)
├── ingest.py                     # (will move later)
├── requirements.txt
├── README.md
├── PROJECT_CONTEXT.md
