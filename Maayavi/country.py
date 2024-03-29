import os
import json

def load_country_data():
    current_dir = os.path.dirname(__file__)  # Get the directory of the current script
    countries_path = os.path.join(current_dir, 'data/countries.json')
    states_path = os.path.join(current_dir, 'data/states.json')
    cities_path = os.path.join(current_dir, 'data/cities.json')

    with open(countries_path, 'r') as f:
        countries_data = json.load(f)
    with open(states_path, 'r') as f:
        states_data = json.load(f)
    with open(cities_path, 'r') as f:
        cities_data = json.load(f)

    countries = {}  # Nested structure
    for country in countries_data:
        country_name = country['country_name'].lower()
        countries[country_name] = country  # Add the entire country data
        countries[country_name]['states'] = {}

    for state in states_data:
        country_name = state['country_name'].lower()
        state_name = state['state_name'].lower()  # Normalize state_name here

        if country_name not in countries:
            continue 
        countries[country_name]['states'][state_name] = state  # Add state with normalized name

    return countries  # We'll now return the expanded data structure

def get_capital(country_name):
    countries = load_country_data()  # Load data every time, in case of updates
    country_norm = country_name.lower()
    if country_norm in countries:
        return countries[country_norm]['capital'] 
    return None 

def get_states(country_name):
    countries = load_country_data()
    country_norm = country_name.lower()
    if country_norm in countries:
        states = countries[country_norm]['states']
        return [state for state in states if states[state]['type'] == 'state'] 
    return None
