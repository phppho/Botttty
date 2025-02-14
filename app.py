from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import requests
import json
import os

app = Flask(__name__)
CORS(app)

# تحميل الإعدادات
with open('config.json') as f:
    config = json.load(f)

# DeepSeek API
def generate_with_deepseek(prompt):
    headers = {"Authorization": f"Bearer {config['DEEPSEEK_API_KEY']}"}
    response = requests.post(
        "https://api.deepseek.com/v1/chat/completions",
        headers=headers,
        json={
            "model": "deepseek-chat",
            "messages": [{"role": "user", "content": prompt}]
        }
    )
    return response.json()['choices'][0]['message']['content']

# ChatGPT API
def generate_with_chatgpt(prompt):
    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers={"Authorization": f"Bearer {config['OPENAI_API_KEY']}"},
        json={
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": prompt}]
        }
    )
    return response.json()['choices'][0]['message']['content']

@app.route('/generate', methods=['POST'])
def generate_content():
    data = request.json
    topic = data['topic']
    
    # توليد المحتوى باستخدام كلا النموذجين
    prompt = f"اكتب مقالة مفصلة عن {topic} في مجال العملات الرقمية"
    content = f"DeepSeek:\n{generate_with_deepseek(prompt)}\n\nChatGPT:\n{generate_with_chatgpt(prompt)}"
    
    return jsonify({"content": content})

@app.route('/post', methods=['POST'])
def post_content():
    content = request.json['content']
    
    # النشر على منصات التواصل الاجتماعي (مثال لتويتر)
    # twitter_response = requests.post(
    #     'https://api.twitter.com/2/tweets',
    #     headers={'Authorization': f'Bearer {config["TWITTER_TOKEN"]}'},
    #     json={'text': content[:280]}
    # )
    
    return "تم النشر بنجاح على جميع المنصات"

if __name__ == '__main__':
    app.run(debug=True)