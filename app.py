from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

BOT_NAME = "Podar CBSE Study AI"

def get_answer(user_msg):
    msg = user_msg.lower()

    # Greetings
    if any(word in msg for word in ["hi", "hello", "hey"]):
        return "Hello 👋 I am Podar CBSE Study AI. Ask me any question from Class 1 to 9."

    # ------------------ MATHS ------------------
    if "fraction" in msg:
        return "A fraction represents a part of a whole. Example: 1/2 means one out of two equal parts."

    if "algebra" in msg:
        return "Algebra uses letters (like x, y) to represent numbers in equations."

    if "linear equation" in msg:
        return "A linear equation is an equation of first degree. Example: 2x + 3 = 7."

    if "pythagoras" in msg:
        return "Pythagoras theorem: In a right triangle, a² + b² = c²."

    if "area of circle" in msg:
        return "Area of circle = πr²"

    # ------------------ SCIENCE ------------------
    if "photosynthesis" in msg:
        return "Photosynthesis is the process by which green plants make food using sunlight, carbon dioxide and water."

    if "force" in msg:
        return "Force is a push or pull that can change shape, direction or speed of an object."

    if "motion" in msg:
        return "Motion is the change in position of an object with respect to time."

    if "atom" in msg:
        return "Atom is the smallest unit of matter."

    if "cell" in msg:
        return "Cell is the basic structural and functional unit of life."

    # ------------------ SOCIAL SCIENCE ------------------
    if "democracy" in msg:
        return "Democracy is a form of government where people elect their leaders."

    if "constitution" in msg:
        return "The Constitution is the supreme law of a country."

    if "latitude" in msg:
        return "Latitude lines run east-west and measure distance from the Equator."

    if "longitude" in msg:
        return "Longitude lines run north-south and measure distance from Prime Meridian."

    if "freedom struggle" in msg:
        return "India’s freedom struggle was the movement to gain independence from British rule in 1947."

    # ------------------ ENGLISH ------------------
    if "noun" in msg:
        return "A noun is the name of a person, place, animal or thing."

    if "verb" in msg:
        return "A verb shows action or state of being."

    if "adjective" in msg:
        return "An adjective describes a noun."

    if "tenses" in msg:
        return "Tenses show time of action: past, present and future."

    # ------------------ COMPUTER ------------------
    if "computer" in msg:
        return "A computer is an electronic machine that processes data."

    if "hardware" in msg:
        return "Hardware refers to physical parts of a computer like keyboard, mouse and monitor."

    if "software" in msg:
        return "Software is a set of programs that tells the computer what to do."

    # ------------------ GENERAL ------------------
    if "thank" in msg:
        return "You're welcome 😊 Keep studying!"

    if "bye" in msg:
        return "Goodbye 👋 Study well!"

    return "📘 I can help with CBSE Class 1–9 Maths, Science, SST, English, Hindi and Computer. Please ask a specific topic."

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
    
