import nltk
from nltk.tokenize import word_tokenize # To add variety to responses
import re # shunting-yard algorithm


knowledge_base = {
    "greetings": [
        "Hello there!", "Hi, how can I help you?", "Good day! What's on your mind?"
    ],
    "self_intro": {
        "what is your name": "My name is Maayavi. It's nice to meet you!",
        "what can you do": "I'm still under development, but I can answer your questions and perform basic calculations for now!"
    },
    "calculations": {
        "add": lambda x, y: x + y,  # Lambda function for addition
        "subtract": lambda x, y: x - y,  # Similar functions for other operations
        "multiply": lambda x, y: x * y,   # Add more operations here
        "divide": lambda x, y: x / y,    # (Be careful about division by zero!) 
    },  # Add a comma here
    "small_talk": [
        "I'm doing well, thanks for asking!",
        "Blue. It's a calm color.",
        "Why did the scarecrow love his job? Because he was outstanding in his field!"  # Example joke
    ],
    "general_questions": [
        "Paris.", "Leonardo da Vinci.",
         "That's a tough one! Philosophers have debated that for centuries.",
         "Berlin, the capital of Germany, is known for its rich history and culture."
    ],
    "about_maayavi": [
    "I'm here to help with calculations and answer your questions!",
    "My creators made me to be a learning AI assistant."  # Add more responses here 
    ]

    }

def get(key, default=None):
    data = {
        "greetings": [ "Hello there!", "Hi, how can I help you?", "Good day! What's on your mind?",],  # Your existing greetings
        "small_talk": ["I'm doing well, thanks for asking!", "Blue. It's a calm color.",],
        "general_questions": ["Paris.", "Leonardo da Vinci.",], 
        "about_maayavi": ["I'm here to help with calculations and answer your questions!",]
    }
    return data.get(key, default)


def convert_to_postfix(expression):
    prec = {'+': 2, '-': 1, '*': 3, '/': 4, '^': 5, '(': 0, '': 9} 
    right_assoc = {'^': True} 
    op_stack = []
    postfix = []
    tokens = re.findall(r'\d+\.\d+|\d+|\S', expression)

    for token in tokens:
        if token.isnumeric():
            postfix.append(token)
        elif token == '(':
            op_stack.append(token)
        elif token == ')':
            while op_stack[-1] != '(':
                postfix.append(op_stack.pop())
            op_stack.pop()  # Remove the '('
        else:  # Operator
            while op_stack and (prec[token] < prec[op_stack[-1]] or (prec[token] == prec[op_stack[-1]] and token in right_assoc)):
                postfix.append(op_stack.pop())
            op_stack.append(token)

    while op_stack:
        postfix.append(op_stack.pop())
    return " ".join(postfix) 


def evaluate_postfix(postfix_expression):
    operations = {"+": lambda x, y: x + y,
                  "-": lambda x, y: x - y,
                  "*": lambda x, y: x * y,
                  "/": lambda x, y: x / y
    } 

    stack = []
    for token in postfix_expression.split():
        if token.isnumeric():
            stack.append(int(token))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = operations[token](operand1, operand2)
            stack.append(result)
    return stack.pop() 


def attempt_calculation(user_input):
    print("Entered attempt_calculation!")  # DEBUG LINE
    # Tokenize the input expression properly
    input_tokens = re.findall(r'\d+|\+|\-|\*|\/', user_input)
    print(input_tokens)  # Check if this is correct

    operations = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y
    }

    try:
        for operator in operations:
            if operator in input_tokens:
                postfix_expression = convert_to_postfix(" ".join(input_tokens))
                result = evaluate_postfix(postfix_expression)
                return str(result)

        return "Sorry, I didn't understand the operation you want me to do."

    except Exception as e:  # Catch any errors in detail
        print("Error:", e)
        return "Sorry, I couldn't understand your calculation request."
