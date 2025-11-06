from flask import Flask, render_template, request, jsonify
import os
from openai import OpenAI  # ✅ Correct import

app = Flask(__name__)

# ✅ Initialize the OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]

    # ✅ Generate chatbot reply
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a friendly and helpful AI chatbot."},
            {"role": "user", "content": user_input}
        ]
    )

    bot_reply = response.choices[0].message.content.strip()
    return jsonify({"reply": bot_reply})


if __name__ == "__main__":
    app.run(debug=True)
