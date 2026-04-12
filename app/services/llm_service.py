import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def generate_text(prompt, model="mistral"):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": model,
            "prompt": prompt,
            "stream": False
        }
    )

    print("\n===== DEBUG =====")
    print("STATUS:", response.status_code)
    print("TEXT:", response.text)
    print("==============\n")

    try:
        data = response.json()
    except Exception:
        return f"Invalid JSON response: {response.text}"

    if "response" in data:
        return data["response"]
    elif "error" in data:
        return f"Ollama error: {data['error']}"
    else:
        return f"Unexpected response format: {data}"
