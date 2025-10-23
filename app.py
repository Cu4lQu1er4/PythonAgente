from flask import Flask, request, jsonify
from openai import OpenAI
import os
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()
client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

@app.route('/')
def home():
    return "Backend IA operativo ✅"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    if not data or 'message' not in data:
        return jsonify({"error": "No se recibió ningún mensaje"}), 400

    user_message = data['message']

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Eres un asistente útil."},
            {"role": "user", "content": user_message}
        ]
    )

    return jsonify({"reply": response.choices[0].message.content})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
