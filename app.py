<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Podar ChatGPT</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>
body {
    margin: 0;
    font-family: Arial, sans-serif;
    background: #f7f7f8;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}

.chat-container {
    width: 100%;
    max-width: 420px;
    height: 90vh;
    background: white;
    display: flex;
    flex-direction: column;
    border-radius: 12px;
    box-shadow: 0 0 20px rgba(0,0,0,0.1);
}

.header {
    background: #10a37f;
    color: white;
    padding: 15px;
    text-align: center;
    font-weight: bold;
    font-size: 18px;
}

.messages {
    flex: 1;
    padding: 15px;
    overflow-y: auto;
}

.message {
    max-width: 75%;
    padding: 10px 14px;
    margin-bottom: 10px;
    border-radius: 10px;
    font-size: 14px;
    line-height: 1.4;
}

.user {
    background: #10a37f;
    color: white;
    margin-left: auto;
    border-bottom-right-radius: 2px;
}

.bot {
    background: #e5e5ea;
    color: black;
    margin-right: auto;
    border-bottom-left-radius: 2px;
}

.input-area {
    display: flex;
    padding: 10px;
    border-top: 1px solid #ddd;
}

input {
    flex: 1;
    padding: 10px;
    font-size: 14px;
    border: 1px solid #ccc;
    border-radius: 6px;
    outline: none;
}

button {
    margin-left: 8px;
    padding: 10px 15px;
    background: #10a37f;
    color: white;
    border: none;
    border-radius: 6px;
    cursor: pointer;
}

button:hover {
    background: #0e8f6f;
}
</style>
</head>

<body>

<div class="chat-container">
    <div class="header">🤖 Podar ChatGPT</div>

    <div class="messages" id="chat">
        <div class="message bot">
            Hello 👋 I am Podar ChatGPT. Ask me anything till Class 10.
        </div>
    </div>

    <div class="input-area">
        <input type="text" id="msg" placeholder="Type your message..." onkeydown="if(event.key==='Enter') send()">
        <button onclick="send()">Send</button>
    </div>
</div>

<script>
function send() {
    let input = document.getElementById("msg");
    let message = input.value.trim();
    if (!message) return;

    let chat = document.getElementById("chat");

    // User message
    let userDiv = document.createElement("div");
    userDiv.className = "message user";
    userDiv.innerText = message;
    chat.appendChild(userDiv);

    chat.scrollTop = chat.scrollHeight;
    input.value = "";

    fetch("/ask", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({message: message})
    })
    .then(res => res.json())
    .then(data => {
        let botDiv = document.createElement("div");
        botDiv.className = "message bot";
        botDiv.innerText = data.reply;
        chat.appendChild(botDiv);
        chat.scrollTop = chat.scrollHeight;
    });
}
</script>

</body>
</html>
