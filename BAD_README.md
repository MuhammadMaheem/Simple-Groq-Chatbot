# AI Chatbot Flask App

A simple Flask-based chatbot using Groq API with a professional frontend.

## Setup

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Create a `.env` file in the project root and add your Groq API key:
   ```
   GROQ_API_KEY=your_actual_api_key_here
   ```

3. Run the application:
   ```
   python app.py
   ```

4. Open your browser and go to `http://127.0.0.1:5000`

## Features

- Clean and professional user interface using Bootstrap
- Real-time chat functionality
- Powered by Groq's fast inference API
- Simple and easy-to-understand code structure

## Project Structure

```
Ai-Chatbot-flask/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html      # Frontend template
└── README.md           # This file
```

## Requirements

- Python 3.7+
- Groq API key (get one from https://groq.com)