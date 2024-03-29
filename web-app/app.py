from flask import Flask, render_template, request, jsonify
from maayavi.maayavi import handle_user_input, greet_user
import sys
sys.path.append('/Users/nithin/Desktop/Maayavi/Maayavi')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    response = handle_user_input(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
