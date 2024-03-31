import re
from sympy import symbols, sympify, solve, sin, cos, tan, log

def shunting_yard(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, 'sin': 4, 'cos': 4, 'tan': 4, 'log': 4}
    right_associative = {'^'}
    output_queue = []
    operator_stack = []

    # Tokenize the expression including variables and functions
    tokens = re.findall(r'\b(?:sin|cos|tan|log)|[a-zA-Z]+|\d+\.\d+|\d+|[()+\-*/^]', expression)

    for token in tokens:
        if re.match(r'\d+\.\d+', token) or re.match(r'\d+', token):
            output_queue.append(float(token))
        elif token.isalpha() or token in ['sin', 'cos', 'tan', 'log']:
            output_queue.append(token)
        elif token in precedence:
            while (operator_stack and operator_stack[-1] != '(' and
                   (precedence[token] < precedence[operator_stack[-1]] or 
                   (precedence[token] == precedence[operator_stack[-1]] and token not in right_associative))):
                output_queue.append(operator_stack.pop())
            operator_stack.append(token)
        elif token == '(':
            operator_stack.append(token)
        elif token == ')':
            while operator_stack and operator_stack[-1] != '(':
                output_queue.append(operator_stack.pop())
            if operator_stack and operator_stack[-1] == '(':
                operator_stack.pop()  # Discard the '('
            else:
                raise ValueError("Mismatched parentheses")
        else:
            raise ValueError(f"Invalid token: {token}")

    while operator_stack:
        if operator_stack[-1] == '(':
            raise ValueError("Mismatched parentheses")
        output_queue.append(operator_stack.pop())

    return output_queue

def evaluate_postfix(postfix_tokens):
    stack = []
    for token in postfix_tokens:
        if isinstance(token, float):
            stack.append(token)
        elif isinstance(token, str) and token.isalpha():
            stack.append(symbols(token))  # Handle symbols
        else:
            if len(stack) < 2:
                raise ValueError("Invalid postfix expression")
            operand2 = stack.pop()
            operand1 = stack.pop()
            if token == '+':
                stack.append(operand1 + operand2)
            elif token == '-':
                stack.append(operand1 - operand2)
            elif token == '*':
                stack.append(operand1 * operand2)
            elif token == '/':
                stack.append(operand1 / operand2)
            elif token == '^':
                stack.append(operand1 ** operand2)
            elif token in ['sin', 'cos', 'tan', 'log']:
                stack.append(operand1)  # Push the operand back for unary operators
                stack.append(eval(f"{token}(operand2)"))  # Evaluate trigonometric/logarithmic functions
    if len(stack) > 1:
        raise ValueError("Invalid postfix expression")
    return stack[0]
