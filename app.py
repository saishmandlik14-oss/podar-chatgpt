from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

HF_API_KEY = os.getenv("HF_API_KEY")
MODEL_URL = "https://api-inference.huggingface.co/models/google/flan-t5-base"

headers = {
    "Authorization": f"Bearer {HF_API_KEY}"
}

@app.route("/")
def home():
    return render_template("chat.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_msg = request.json.get("message", "")
    if not user_msg:
        return jsonify({"reply": "Ask something."})

    payload = {
        "inputs": f"Answer like a Class 10 teacher: {user_msg}"
    }

    response = requests.post(MODEL_URL, headers=headers, json=payload)

    if response.status_code != 200:
        return jsonify({"reply": "AI is busy, try again later."})

    data = response.json()
    return jsonify({"reply": data[0]["generated_text"]})

if __name__ == "__main__":
    app.run()
