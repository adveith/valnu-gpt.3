from flask import Flask, request, jsonify, render_template
from chatbot import chatbot_response  # Import the chatbot_response function

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message")
    response = chatbot_response(user_input)  # Call the chatbot_response function
    return jsonify({"response": response})  # Return response in JSON format

if __name__ == '__main__':
    app.run(debug=True)
