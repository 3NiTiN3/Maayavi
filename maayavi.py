import random 
import nltk
from nltk.tokenize import word_tokenize # To add variety to responses
import knowledge_base 
import re

def greet_user():
    greetings = knowledge_base.get("greetings", ["Hello!"])  # Fetch greetings from knowledge base
    print(random.choice(greetings))  # Select a random greeting




def greet_user():
    print("Hello! I'm Maayavi, your friendly intelligence. How can I help you?")




def handle_user_input(user_input):
    print("Inside handle_user_input with input:", user_input)  # DEBUG LINE 
    # Preprocess user input (lowercase, remove punctuation, etc.)
    processed_input = word_tokenize(user_input.lower())

    # Identify keywords or patterns in the input
    if any(word in processed_input for word in ["hello", "hi", "hey"]):
        return random.choice(knowledge_base["greetings"])
    elif any(word in processed_input for word in ["name", "call"]):
        return knowledge_base["self_intro"]["what is your name"]
    # Detect Calculation Requests (Example)
    calc_keywords = ["calculate", "add", "subtract", "multiply", "divide", "solve"]  # Expanded keywords
    if any(word in word_tokenize(user_input.lower()) for word in calc_keywords):
        print("Calculation request detected!")  # DEBUG LINE
        calculation_result = knowledge_base.attempt_calculation(user_input)  # Call the function from knowledge_base 
        return calculation_result
        # Detect subtraction requests
    elif re.search(r'subtract\s+\d+\s+from\s+\d+', user_input):
        print("Subtraction request detected!")  # DEBUG LINE
        # Handle the subtraction request here
    else:
        return "I'm still learning, but I don't quite understand that yet."







# Get user input and handle it
user_input = input("You: ")
response = handle_user_input(user_input)
print("Maayavi:", response)

# Very basic start for now!
if __name__ == "__main__":
    greet_user()


    # Create a loop for continuous interaction:
    while True: 
        user_input = input("You: ")

        # Stop the conversation if the user says something like "quit" or "exit"
        if user_input.lower() in ["quit", "exit", "bye", "goodbye"]:
            print("Maayavi: Farewell! Let me know if I can help you with anything else in the future.")
            break

        response = handle_user_input(user_input)
        print("Maayavi:", response)

        # Add a prompt for further questions
        if "Calculation request detected!" in response: 
            print("Maayavi: Would you like to make another calculation, or can I help with something else?")
