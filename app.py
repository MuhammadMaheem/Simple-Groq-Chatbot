from flask import Flask, render_template, request, jsonify
import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Initialize Groq client with API key from environment variable
client = Groq(api_key=os.environ.get('GROQ_API_KEY'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data['message']
    
    # Call Groq API
    response = client.chat.completions.create(
        model="moonshotai/kimi-k2-instruct-0905",
        messages=[{"role": "user", "content": message}]
    )
    
    reply = response.choices[0].message.content
    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(debug=True)