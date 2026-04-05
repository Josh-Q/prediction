import requests
from config.config import OLLAMA_API_KEY, MODEL_NAME   
import json

def call_model(prompt):
    try:
        response = requests.post(
            "https://ollama.com/api/generate",
            headers={"Authorization": f"Bearer {OLLAMA_API_KEY}"},
            json={"model": MODEL_NAME, "prompt": prompt, "stream": False},
            timeout=10
        )

        data = response.json()["response"].strip()
        return data

    except Exception as e:
        print("Error:", e)
        return {"prediction": "NEGATIVE", "confidence": 0.0}

