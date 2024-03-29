import random 
import nltk
from nltk.tokenize import word_tokenize # To add variety to responses
import country
import re
import knowledge_base
import pandas as pd
import sys

def greet_user():
    print("Hello! I'm Maayavi, your friendly intelligence. How can I help you?")

def handle_user_input(user_input):
   
    # Preprocess user input (lowercase, remove punctuation, etc.)
    processed_input = word_tokenize(user_input.lower())

    # Default if no match found

    # Favorite Color Question (Should be checked first)
    if re.search(r'\b(favorite\s+color)\b', user_input.lower()):  
        return random.choice(knowledge_base.get("small_talk"))

    # Small Talk Patterns
    if re.search(r'(how\s+are\s+you|how\'s\s+it\s+going)', user_input.lower()):
        return random.choice(knowledge_base.get("small_talk"))
    # ... (Add the other small talk regex patterns here) ...

    # Detect Calculation Requests (Example)
    calc_keywords = ["calculate", "add", "subtract", "multiply", "divide", "solve"]  # Expanded keywords
    if any(word in word_tokenize(user_input.lower()) for word in calc_keywords):
        
        calculation_result = knowledge_base.attempt_calculation(user_input)  # Call the function from knowledge_base 
        return calculation_result
        # Detect subtraction requests
    elif re.search(r'subtract\s+\d+\s+from\s+\d+', user_input):
        print("Subtraction request detected!")  # DEBUG LINE
        # Handle the subtraction request here

    # Capital city 
    if re.search(r'capital\s+of\s+(.*)', user_input.lower()):
        country_name = re.search(r'capital\s+of\s+(.*)', user_input.lower()).group(1)  
        capital_city = country.get_capital(country_name) 
        if capital_city:
            return "The capital of {} is {}.".format(country_name, capital_city)
        else:
            return "I don't have information about the capital of {}.".format(country_name)

    # Questions about states
    if re.search(r'what\s+are\s+the\s+states\s+in\s+(.*)', user_input.lower()):
        country_name = re.search(r'what\s+are\s+the\s+states\s+in\s+(.*)', user_input.lower()).group(1) 
        states = country.get_states(country_name)
        if states:
            return "The states in {} are: {}".format(country_name, ', '.join(states))
        else:
            return "I couldn't find states for {}".format(country_name)

    # General Knowledge Patterns
    if re.search(r'what\s+the\s+(.*)', user_input.lower()):  
        return random.choice(knowledge_base.get("general_questions")) 
    # ... (Add more general knowledge regex patterns here) ...

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


