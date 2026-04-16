import requests

# URL where your FastAPI AI Core is running
AI_CORE_URL = "http://127.0.0.1:8000/generate"

def get_ai_insight(prompt):
    """
    Sends the prepared prompt to the AI Core API
    and retrieves the generated insight.

    Args:
        prompt (str): The input prompt for the LLM

    Returns:
        str: AI-generated response
    """

    # Make POST request to your AI Core
    response = requests.post(
        AI_CORE_URL,
        json={
            "prompt": prompt,
            "model": "mistral",              # Default model
            "collection": "laptop_metrics"   # Enables RAG context
        }
    )

    # Extract response from API JSON output
    return response.json()["response"]
