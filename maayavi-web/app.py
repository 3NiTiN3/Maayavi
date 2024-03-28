from flask import Flask, jsonify, request
from maayavi import get_capital, get_states 

app = Flask(__name__)

# Replace this with Maayavi's logic
@app.route('/ask', methods=['POST'])
def process_query():
    user_question = request.json['question']
    # Process the question using Maayavi's existing logic
    answer = "I'm still learning, but I'm working on it!"  # Replace this!
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True) 
