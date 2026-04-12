# AI Core - Local LLM Service

## 🚀 Overview
AI Core is a local-first AI platform that exposes LLM capabilities via APIs.  
It enables building reusable enterprise AI applications like RFP copilots, cloud advisors, and executive assistants.

## 🧠 Architecture
Client Apps → AI Core API → Ollama → Local LLM

## 🔧 Tech Stack
- FastAPI
- Ollama (local LLM runtime)
- LLaMA / Mistral models

## 📌 Features
- `/generate` → text generation
- Modular architecture for reuse
- Local-first (no external API dependency)

## ▶️ Getting Started

### 1. Install Ollama
https://ollama.com

```bash
ollama run llama3
