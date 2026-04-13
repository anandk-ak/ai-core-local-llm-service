import requests
import time
from app.services.rag_service import retrieve_context

OLLAMA_URL = "http://localhost:11434/api/generate"

def generate_text(prompt, model="mistral", collection=None):
    start_time = time.time()

    print(f"[LLM REQUEST] model={model} | collection={collection} | prompt_length={len(prompt)}")

    # RAG logic: First RAG is called and then the LLM
    if collection:
        context = retrieve_context(collection, prompt)
        print(f"[RAG] Retrieved context: {context}")

        if context:
            prompt = f"""
Context:
{context}

User Query:
{prompt}
"""

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": model,
                "prompt": prompt,
                "stream": False
            }
        )

        duration = round(time.time() - start_time, 2)
        print(f"[LLM RESPONSE] status={response.status_code} | time={duration}s")

        data = response.json()

        if "response" in data:
            return data["response"]

        elif "error" in data:
            print(f"[LLM ERROR] {data['error']}")
            return f"Ollama error: {data['error']}"

        else:
            print(f"[LLM UNKNOWN FORMAT] {data}")
            return f"Unexpected response format: {data}"

    except Exception as e:
        print(f"[LLM EXCEPTION] {str(e)}")
        return f"LLM connection error: {str(e)}"
