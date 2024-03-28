from flask import Flask, jsonify, request
import sys
sys.path.append('/Users/nithin/Desktop/Maayavi')
from maayavi.maayavi import handle_user_input  # Adjust the import path

app = Flask(__name__)

@app.route('/ask', methods=['POST'])
def process_query():
    user_question = request.json['question']
    # Process the question using Maayavi's logic
    answer = handle_user_input(user_question)
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)
