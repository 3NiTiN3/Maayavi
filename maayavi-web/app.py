from maayavi import handle_user_input
from maayavi.knowledge_base import get  
from maayavi.country import get_capital, get_states
from flask import Flask


app = Flask(__name__)

@app.route('/ask', methods=['POST'])
def index():
    # Example:
    user_input = "Hello"
    response = maayavi.handle_user_input(user_input)
    return response


def process_query():
    user_question = request.json['question']
    # Process the question using Maayavi's logic
    answer = handle_user_input(user_question)
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)
