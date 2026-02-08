from flask import Flask, render_template, request, jsonify
import openai
import os

app = Flask(__name__)

# DEBUG: check if key is loaded
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("ERROR: OPENAI_API_KEY not found!")
else:
    print("OPENAI_API_KEY found ✅")  # This will appear in Render logs

openai.api_key = api_key

@app.route("/")
def home():
    return render_template("chat.html")

@app.route("/ask", methods=["POST"])
def ask():
    try:
        user_msg = request.json.get("message", "")
        if not user_msg:
            return jsonify({"reply": "Please type a question."})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are Podar ChatGPT, a helpful Class 10 school assistant."},
                {"role": "user", "content": user_msg}
            ]
        )

        return jsonify({"reply": response.choices[0].message.content})

    except Exception as e:
        print("OpenAI Error:", e)  # Print the exact error in logs
        return jsonify({"reply": "Error connecting AI"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
