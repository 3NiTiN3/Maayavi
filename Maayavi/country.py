import os
import json

current_dir = os.path.dirname(__file__)
countries_path = os.path.join(current_dir, 'data/countries.json')
states_path = os.path.join(current_dir, 'data/states.json')
cities_path = os.path.join(current_dir, 'data/cities.json')

with open(countries_path, 'r') as f:
    countries_data = json.load(f)
with open(states_path, 'r') as f:
    states_data = json.load(f)
with open(cities_path, 'r') as f:
    cities_data = json.load(f)

countries = {}
for country in countries_data:
    country_name = country['country_name'].lower()
    countries[country_name] = {
        'info': country,
        'states': {},
        'cities': []
    }

for state in states_data:
    country_name = state['country_name'].lower()
    state_name = state['state_name'].lower()
    if country_name in countries:
        countries[country_name]['states'][state_name] = state

for city in cities_data:
    country_name = city['country_name'].lower()
    state_name = city['state_name'].lower()
    if country_name in countries:
        countries[country_name]['cities'].append(city)
        if state_name in countries[country_name]['states']:
            if 'cities' not in countries[country_name]['states'][state_name]:
                countries[country_name]['states'][state_name]['cities'] = []
            countries[country_name]['states'][state_name]['cities'].append(city)

def get_capital(country_name):
    return countries.get(country_name.lower(), {}).get('info', {}).get('capital')

def get_states(country_name):
    return list(countries.get(country_name.lower(), {}).get('states', {}).keys())

def get_cities(state_name, country_name):
    country_norm = country_name.lower()
    state_norm = state_name.lower()
    return countries.get(country_norm, {}).get('states', {}).get(state_norm, {}).get('cities')

def get_cities_in_country(country_name):
    return [city['city_name'] for city in countries.get(country_name.lower(), {}).get('cities', [])]

def find_country_by_city(city_name):
    for country, data in countries.items():
        if any(city['city_name'].lower() == city_name.lower() for city in data['cities']):
            return country
    return None

def get_cities(state_name, country_name):
    for country, data in countries.items():
        if country.lower() == country_name.lower():
            state_data = data['states'].get(state_name.lower())
            if state_data:
                return [city['city_name'] for city in state_data.get('cities', [])]
    return []

def find_country_by_state(state_name):
    for country, data in countries.items():
        if state_name.lower() in data['states']:
            return country
    return None

def find_state_by_city(city_name):
    for city in cities_data:
        if city['city_name'].lower() == city_name.lower():
            return city['state_name']
    return None

