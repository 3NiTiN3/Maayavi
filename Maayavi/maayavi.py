import random
import nltk
from nltk.tokenize import word_tokenize
import country  # Ensure this module is implemented properly
import re
from knowledge_base import get_response # Make sure this file exists with proper data structure
from shunting import shunting_yard, evaluate_postfix

def greet_user():
    print("Hello! I'm Maayavi, your friendly intelligence. How can I help you?")

def preprocess_input(user_input):
    return word_tokenize(user_input.lower())

def handle_country_queries(processed_input, user_input):
    # Handle query for capital
    match = re.search(r'capital\s+of\s+(.*)', user_input)
    if match:
        country_name = match.group(1)
        capital_city = country.get_capital(country_name)
        if capital_city:
            return f"The capital of {country_name} is {capital_city}."
        else:
            return f"I don't have information about the capital of {country_name}."

    # Handle query for states
    match = re.search(r'states\s+of\s+([^\s]+)', user_input)
    if match:
        country_name = match.group(1)
        states = country.get_states(country_name)
        if states:
            return f"The states in {country_name} are: {', '.join(states)}"
        else:
            return f"I couldn't find states for {country_name}"
    
    # Find the Country of a Given City
    if 'which country is' in user_input:
        match = re.search(r'which country is\s+([^\s]+)', user_input)
        if match:
            city_name = match.group(1)
            country_name = country.find_country_by_city(city_name)
            if country_name:
                return f"{city_name} is in {country_name}."
            else:
                return f"I couldn't find the country for {city_name}."

    # List Cities in a Given State
    # Handling 'cities in [country]'
    match = re.search(r'cities in ([\w\s]+)', user_input, re.IGNORECASE)
    if match:
        country_name = match.group(1).strip().lower()
        cities = country.get_cities_in_country(country_name)
        if cities:
            return f"The cities in {country_name.capitalize()} are: {', '.join(cities)}"
        else:
            return f"I couldn't find cities for {country_name.capitalize()}."

    # Handling 'cities of [country]'
    match = re.search(r'cities of ([\w\s]+)', user_input, re.IGNORECASE)
    if match:
        country_name = match.group(1).strip().lower()
        # Convert country name to proper title case for display and matching
        country_name_title = country_name.title()
        cities = country.get_cities_in_country(country_name_title)
        if cities:
            return f"The cities in {country_name_title} are: {', '.join(cities)}"
        else:
            return f"I couldn't find cities for {country_name_title}."

    # Handling 'states in [country]'
    match = re.search(r'states in ([\w\s]+)', user_input, re.IGNORECASE)
    if match:
        country_name = match.group(1).strip().lower()
        states = country.get_states(country_name)
        if states:
            return f"The states in {country_name.capitalize()} are: {', '.join(states)}"
        else:
            return f"I couldn't find states for {country_name.capitalize()}."


    # Find the State for a Given City
    if 'which state is' in user_input:
        match = re.search(r'which state is\s+([^\s]+)', user_input)
        if match:
            city_name = match.group(1).strip()
            state_name = country.find_state_by_city(city_name)
            if state_name:
                return f"{city_name} is in {state_name} state."
            else:
                return f"I couldn't find the state for {city_name}."


def handle_small_talk(processed_input):
    if any(re.search(pattern, ' '.join(processed_input)) for pattern in ['how are you', "how's it going"]):
        return random.choice(knowledge_base.get("small_talk"))

def handle_general_knowledge(processed_input):
    if 'what' in processed_input:
        return random.choice(knowledge_base.get("general_questions"))

def attempt_calculation(user_input, processed_input):
    input_tokens = re.findall(r'\d+|\+|\-|\*|\/', user_input)

    calc_keywords = ["calculate", "add", "subtract", "multiply", "divide", "solve"]
    if any(word in processed_input for word in calc_keywords):
        try:
            if user_input.lower().startswith("solve"):
                user_input = user_input[len("solve"):]
            postfix_tokens = shunting_yard(user_input)
            result = evaluate_postfix(postfix_tokens)
            return str(result)
        except Exception as e:
            print(f"Error: {e}")
            return "Sorry, I couldn't understand your calculation request."
    return "I'm still learning, but I don't quite understand that yet."

def handle_user_input(user_input):
    processed_input = preprocess_input(user_input)
    
    # Check the knowledge base first for a direct response
    direct_response = get_response(' '.join(processed_input))
    if direct_response:
        return direct_response

    # If not found, proceed with other processing
    response = handle_country_queries(processed_input, user_input) or \
               handle_small_talk(processed_input) or \
               handle_general_knowledge(processed_input) or \
               attempt_calculation(user_input, processed_input)

    return response if response else "I'm still learning, but I don't quite understand that yet."

if __name__ == "__main__":
    greet_user()
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye", "goodbye"]:
            print("Maayavi: Farewell! Let me know if I can help you with anything else in the future.")
            break
        response = handle_user_input(user_input)
        print(f"Maayavi: {response}")
