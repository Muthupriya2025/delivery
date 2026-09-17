# Delivery App AI Chatbot

Flask frontend + Python backend + Google Gemini API.

## Project Structure

delivery_app_gemini_chatbot/
│
├── app.py
├── requirements.txt
├── .env.example
├── README.md
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css

## Setup

### 1. Install Python

Use Python 3.10 or newer.

### 2. Create virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add Gemini API key

Create a `.env` file in the project folder:

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

Replace `YOUR_GEMINI_API_KEY` with your actual Gemini API key.

### 5. Run the chatbot

```bash
python app.py
```

### 6. Open in browser

```text
http://127.0.0.1:5000
```

## Features

- Flask frontend
- Python backend
- Google Gemini API
- Delivery domain-specific system prompt
- Chat history
- Responsive chat UI
- Error handling
- API key stored in `.env`

Never upload your real `.env` file or API key to GitHub.
