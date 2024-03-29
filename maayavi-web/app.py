from flask import Flask, render_template, request
from Maayavi.maayavi import handle_user_input

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_input', methods=['POST'])
def process_input():  # Now correctly indented!
    user_input = request.form['userInput']
    response = handle_user_input(user_input)
    return response

if __name__ == "__main__":
    app.run(debug=True)
