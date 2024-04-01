from flask import Flask, render_template, request, jsonify
import json
import os
from maayavi import handle_user_input


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form['message']
    response = handle_user_input(user_input)
    return jsonify({'reply': response})

@app.route('/train', methods=['POST'])
def train():
    question = request.form['question']
    answer = request.form['answer']
    file_path = 'Maayavi/training_data.json'

    if not os.path.isfile(file_path):
        with open(file_path, 'w') as file:
            json.dump([], file)

    with open(file_path, 'r') as file:
        data = json.load(file)

    data.append({'question': question, 'answer': answer})

    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

    return jsonify({'status': 'success', 'message': 'Training data added successfully.'})

if __name__ == '__main__':
    app.run(debug=True)
