import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def generate_text(prompt, model="llama3"):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": model,
            "prompt": prompt,
            "stream": False
        }
    )

    print("\n===== DEBUG START =====")
    print("STATUS CODE:", response.status_code)
    print("RAW TEXT:", response.text)
    print("JSON:", response.json())
    print("===== DEBUG END =====\n")

    data = response.json()

    if "response" in data:
        return data["response"]
    elif "error" in data:
	return f"Ollama error: {data['error']}"

import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def generate_text(prompt, model="llama3:latest"):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": model,
            "prompt": prompt,
            "stream": False
        }
    )

    # 👇 DEBUG (keep this for now)
    print("\n===== DEBUG =====")
    print("STATUS:", response.status_code)
    print("TEXT:", response.text)
    print("==============\n")

    try:
        data = response.json()
    except Exception:
        return f"Invalid JSON response: {response.text}"

    # 👇 SAFE HANDLING
    if "response" in data:
        return data["response"]
    elif "error" in data:
        return f"Ollama error: {data['error']}"
    else:
        return f"Unexpected response format: {data}"        return f"Ollama error: {data['error']}"
    else:
        return f"Unexpected response: {data}"

import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def generate_text(prompt, model="llama3:latest"):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": model,
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json()["response"]
