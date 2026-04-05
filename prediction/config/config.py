import os
from dotenv import load_dotenv

load_dotenv()

OLLAMA_API_KEY = os.getenv("OLLAMA_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME")