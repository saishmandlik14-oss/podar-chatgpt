from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

BOT_NAME = "Podar CBSE Study AI"

def get_answer(user_msg):
    msg = user_msg.lower()

    # ---------------- GREETINGS ----------------
    if any(word in msg for word in ["hi", "hello", "hey"]):
        return "Hello 👋 I am Podar CBSE Study AI. Ask me any question from Class 1 to 9."

    if "your name" in msg:
        return "My name is Podar CBSE Study AI 🤖"

    # ================== MATHS ==================

    if "square root" in msg:
        return "Square root is a number which when multiplied by itself gives the original number. Example: √25 = 5."

    if "fraction" in msg:
        return "A fraction represents part of a whole. Example: 1/2."

    if "lcm" in msg:
        return "LCM means Least Common Multiple."

    if "hcf" in msg:
        return "HCF means Highest Common Factor."

    if "prime number" in msg:
        return "A prime number has only 2 factors: 1 and itself."

    if "even number" in msg:
        return "An even number is divisible by 2."

    if "odd number" in msg:
        return "An odd number is not divisible by 2."

    if "area" in msg:
        return "Area is the space inside a shape."

    if "perimeter" in msg:
        return "Perimeter is the total boundary length of a shape."

    if "triangle" in msg:
        return "A triangle has 3 sides and 3 angles."

    if "rectangle" in msg:
        return "A rectangle has 4 sides and opposite sides are equal."

    # ================== SCIENCE ==================

    if "photosynthesis" in msg:
        return "Photosynthesis is the process by which plants make food using sunlight."

    if "respiration" in msg:
        return "Respiration is the process of releasing energy from food."

    if "force" in msg:
        return "Force is a push or pull."

    if "motion" in msg:
        return "Motion is change in position of an object."

    if "gravity" in msg:
        return "Gravity is the force that pulls objects towards Earth."

    if "atom" in msg:
        return "Atom is the smallest unit of matter."

    if "cell" in msg:
        return "Cell is the basic unit of life."

    if "human heart" in msg:
        return "The human heart pumps blood throughout the body."

    if "solar system" in msg:
        return "The solar system consists of the Sun and 8 planets."

    if "planet" in msg:
        return "A planet is a celestial body that revolves around the Sun."

    # ================== SOCIAL SCIENCE ==================

    if "democracy" in msg:
        return "Democracy is a government of the people, by the people, for the people."

    if "constitution" in msg:
        return "The Constitution is the supreme law of India."

    if "latitude" in msg:
        return "Latitude measures distance from the Equator."

    if "longitude" in msg:
        return "Longitude measures distance from the Prime Meridian."

    if "continent" in msg:
        return "There are 7 continents in the world."

    if "freedom fighters" in msg:
        return "Some Indian freedom fighters are Mahatma Gandhi, Subhash Chandra Bose and Bhagat Singh."

    if "capital of india" in msg:
        return "The capital of India is New Delhi."

    # ================== ENGLISH ==================

    if "noun" in msg:
        return "A noun is the name of a person, place, animal or thing."

    if "verb" in msg:
        return "A verb shows action."

    if "adjective" in msg:
        return "An adjective describes a noun."

    if "pronoun" in msg:
        return "A pronoun replaces a noun."

    if "sentence" in msg:
        return "A sentence is a group of words that makes complete sense."

    if "alphabet" in msg:
        return "There are 26 letters in the English alphabet."

    # ================== COMPUTER ==================

    if "computer" in msg:
        return "A computer is an electronic machine."

    if "hardware" in msg:
        return "Hardware means physical parts of computer."

    if "software" in msg:
        return "Software means programs used in computer."

    if "cpu" in msg:
        return "CPU is the brain of the computer."

    if "input device" in msg:
        return "Keyboard and mouse are input devices."

    if "output device" in msg:
        return "Monitor and printer are output devices."

    # ================== GENERAL GK ==================

    if "national animal" in msg:
        return "The national animal of India is Tiger."

    if "national bird" in msg:
        return "The national bird of India is Peacock."

    if "national flower" in msg:
        return "The national flower of India is Lotus."

    if "independence day" in msg:
        return "India celebrates Independence Day on 15 August."

    if "republic day" in msg:
        return "India celebrates Republic Day on 26 January."

    if "thank" in msg:
        return "You're welcome 😊 Keep studying!"

    if "bye" in msg:
        return "Goodbye 👋 Study well!"

    return "📘 Ask me short CBSE questions from Class 1 to 9 (Maths, Science, SST, English, Computer, GK)."
    
