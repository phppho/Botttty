from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TWITTER_TOKEN = os.getenv("TWITTER_TOKEN")

# DeepSeek API
def generate_with_deepseek(prompt):
    headers = {"Authorization": f"Bearer {DEEPSEEK_API_KEY}"}
    response = requests.post(
        "https://api.deepseek.com/v1/chat/completions",
        headers=headers,
        json={"model": "deepseek-chat", "messages": [{"role": "user", "content": prompt}]}
    )
    return response.json().get('choices', [{}])[0].get('message', {}).get('content', '')

# ChatGPT API
def generate_with_chatgpt(prompt):
    headers = {"Authorization":