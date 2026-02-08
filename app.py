from flask import Flask, render_template, request, jsonify
import openai
import os

app = Flask(__name__)

# Read the API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def home():
    return render_template("chat.html")

@app.route("/ask", methods=["POST"])
def ask():
    try:
        user_msg = request.json.get("message", "")

        if not user_msg:
            return jsonify({"reply": "Please type a question."})

        # Call OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are Podar ChatGPT, a helpful Class 10 school assistant."},
                {"role": "user", "content": user_msg}
            ]
        )

        # Return the AI's reply
        return jsonify({"reply": response.choices[0].message.content})

    except Exception as e:
        # Return error message if something fails
        return jsonify({"reply": "Error connecting AI"})

# Only used if running locally
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
