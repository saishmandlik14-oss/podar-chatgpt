from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

BOT_NAME = "Podar ChatGPT"

# OFFLINE QUESTION–ANSWER DATA
qa_data = {
    # Normal conversation
    "hi": "Hello 👋 I am Podar ChatGPT. How can I help you?",
    "hello": "Hi there 😊 I am Podar ChatGPT.",
    "how are you": "I am fine and ready to help you 📚",
    "what is your name": "My name is Podar ChatGPT 🤖",
    "who made you": "I was created as a school project to help students till Class 10.",
    "thank you": "You're welcome 😊",
    "bye": "Goodbye 👋 Have a nice day!",

    # Class 1–5
    "what is computer": "A computer is an electronic machine that helps us work and learn.",
    "what is addition": "Addition means adding numbers together.",
    "what is subtraction": "Subtraction means taking one number away from another.",

    # Class 6–8
    "what is photosynthesis": "Photosynthesis is the process by which plants make food using sunlight.",
    "what is force": "Force is a push or pull that can change the shape or motion of an object.",
    "what is noun": "A noun is the name of a person, place, animal or thing.",

    # Class 9–10
    "what is newton first law": "An object remains at rest or in motion unless acted upon by an external force.",
    "what is democracy": "Democracy is a form of government where people elect their leaders.",
    "what is algebra": "Algebra is a branch of mathematics that uses letters and numbers."
}

def get_answer(user_msg):
    user_msg = user_msg.lower().strip()

    for question, answer in qa_data.items():
        if question in user_msg:
            return answer

    return "Sorry 😔 I don't know this yet. Ask me a Class 1–10 question."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_message = request.json.get("message", "")
    reply = get_answer(user_message)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
    
