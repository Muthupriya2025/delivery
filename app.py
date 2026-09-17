import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from google import genai

load_dotenv()

app = Flask(__name__)

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError("GEMINI_API_KEY is missing. Add it to the .env file.")

client = genai.Client(api_key=api_key)

SYSTEM_PROMPT = """You are a helpful Delivery App AI Assistant.
Help users with food delivery, parcel delivery, order status, delivery charges,
addresses, estimated delivery guidance, cancellations, returns, and general
delivery-app questions.

Do not invent real-time order status, tracking numbers, prices, restaurant
availability, or account information. If real-time information is required,
tell the user to check the delivery app or contact support.
Keep answers clear, friendly, and concise.
"""

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    message = (data.get("message") or "").strip()
    history = data.get("history") or []

    if not message:
        return jsonify({"error": "Please enter a message."}), 400

    conversation = SYSTEM_PROMPT + "\n\nConversation:\n"

    for item in history[-10:]:
        role = item.get("role", "user")
        text = item.get("text", "")
        conversation += f"{role}: {text}\n"

    conversation += f"user: {message}\nassistant:"

    try:
        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=conversation
        )

        reply = response.text or "Sorry, I could not generate a response."
        return jsonify({"reply": reply})

    except Exception as exc:
        return jsonify({"error": f"Gemini API error: {exc}"}), 500


if __name__ == "__main__":
    app.run(debug=True)
