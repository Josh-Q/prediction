import requests
from config import OLLAMA_API_KEY, MODEL_NAME    

import os
from ollama import Client

client = Client(
    host="https://ollama.com",
    headers={'Authorization': 'Bearer ' + OLLAMA_API_KEY}
)

messages = [
  {
    'role': 'user',
    'content': 'Why is the sky blue?',
  },
]

for part in client.chat(MODEL_NAME, messages=messages, stream=True):
  print(part['message']['content'], end='', flush=True)