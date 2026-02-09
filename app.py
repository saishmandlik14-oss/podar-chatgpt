from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("chat.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    msg = data.get("message", "")
    return jsonify({
        "reply": f"Server is working ✅ You said: {msg}"
    })

if __name__ == "__main__":
    app.run(debug=True)
