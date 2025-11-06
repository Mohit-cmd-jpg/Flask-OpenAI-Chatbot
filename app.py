# Import necessary libraries
from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import os
import time

# Initialize OpenAI client
client = OpenAI(api_key="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")

# Chatbot name and role
name = "MohitBot"
role = "helpful AI web assistant"

# Define role instructions
impersonated_role = f"""
You are {name}, a {role}.
Always reply helpfully and conversationally.
Keep answers short, clear, and friendly.
You are not an AI model — you’re {name}, Mohit’s assistant.
"""

# Initialize chat history
chat_history = ""

# Create Flask app
app = Flask(__name__)

# Function to get model response
def chatcompletion(user_input, chat_history):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=1,
        messages=[
            {"role": "system", "content": f"{impersonated_role}. Conversation history: {chat_history}"},
            {"role": "user", "content": user_input},
        ],
    )
    return response.choices[0].message.content.strip()

# Handle user input
def get_response(user_input):
    global chat_history
    bot_reply = chatcompletion(user_input, chat_history)
    chat_history += f"\nUser: {user_input}\n{name}: {bot_reply}\n"
    return bot_reply

# Routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get("msg")
    return jsonify({"reply": get_response(userText)})

# Run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
