import json
from transformers import GPT2LMHeadModel, GPT2Tokenizer
# knowledge_base.py

knowledge_base = {
    "greetings": [
        "Hello there!", "Hi, how can I help you?", "Good day! What's on your mind?"
    ],
    "self_intro": {
        "what is your name": "My name is Maayavi. It's nice to meet you!",
        "what can you do": "I'm still under development, but I can answer your questions and perform basic calculations for now!"
    },
    "small_talk": [
        "I'm doing well, thanks for asking!",
    ],
    "general_questions": [
        "That's a tough one! Philosophers have debated that for centuries.",
        "Berlin, the capital of Germany, is known for its rich history and culture."
        # Consider adding more responses here.
    ],
    "about_maayavi": [
        "I'm here to help with calculations and answer your questions!",
        "My creators made me to be a learning AI assistant."
        # Add more responses here.
    ]
}

def get(key, default=None):
    return knowledge_base.get(key, default)


def load_training_data():
    try:
        with open('Maayavi/training_data.json', 'r') as file:
            training_data = json.load(file)
            for item in training_data:
                question = item['question'].lower()
                answer = item['answer']
                knowledge_base[question] = answer
    except FileNotFoundError:
        print("The training_data.json file was not found. Continuing with the default knowledge base.")

load_training_data()

def get_response(question, default=None):
    return knowledge_base.get(question.lower(), default)