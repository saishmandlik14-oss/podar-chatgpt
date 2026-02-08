import openai

response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are Podar ChatGPT, a helpful Class 10 school assistant."},
        {"role": "user", "content": user_msg}
    ]
)
reply = response.choices[0].message.content

