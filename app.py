from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

BOT_NAME = "Podar ChatGPT"

# NORMAL CONVERSATION DATA
qa_data = {
    "hi": "Hello 👋 I am Podar ChatGPT. Nice to meet you!",
    "hello": "Hi 😊 How can I help you today?",
    "hey": "Hey! 👋 What’s up?",
    "how are you": "I’m doing great 😄 Thanks for asking!",
    "what is your name": "My name is Podar ChatGPT 🤖",
    "who are you": "I am Podar ChatGPT, a friendly offline chatbot.",
    "what can you do": "I can chat with you, talk politely, and keep you company 😊",
    "good morning": "Good morning 🌞 Have a great day!",
    "good afternoon": "Good afternoon 🌤️ Hope your day is going well!",
    "good evening": "Good evening 🌆 How was your day?",
    "good night": "Good night 🌙 Sleep well!",
    "thank you": "You're welcome 😊",
    "thanks": "Happy to help 😄",
    "bye": "Bye 👋 Take care!",
    "see you": "See you soon 👋",
    "i am sad": "I’m sorry to hear that 😔 I’m here to listen.",
    "i am happy": "That’s great 😄 I’m happy for you!",
    "do you like me": "Of course 😊 You are nice to talk to!",
    "are you real": "I am not human, but I am real as a chatbot 🤖",
    "help me": "Sure! Tell me what you need help with 🙂"
}

def get_answer(user_msg):
    user_msg = user_msg.lower().strip()

    for question, answer in qa_data.items():
        if question in user_msg:
            return answer

    return "😊 I’m here to chat! Say hi, ask how I am, or just talk to me."

@app.route("/")
def home():
    return render_template("chat.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_message = request.json.get("message", "")
    reply = get_answer(user_message)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
