import nltk
import json
import random
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import TreebankWordTokenizer

# Download required resources
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

# Init
lemmatizer = WordNetLemmatizer()
tokenizer = TreebankWordTokenizer()

# Load intents
with open('intents.json') as file:
    intents = json.load(file)

# Preprocess
def clean_sentence(sentence):
    words = tokenizer.tokenize(sentence.lower())
    return [lemmatizer.lemmatize(w) for w in words]

# Get response
def get_response(user_input):
    user_words = clean_sentence(user_input)
    for intent in intents['intents']:
        for pattern in intent.get('patterns', []):
            pattern_words = clean_sentence(pattern)
            if set(user_words) & set(pattern_words):
                return random.choice(intent['responses'])
    no_match = next(i for i in intents['intents'] if i['tag'] == 'no_match')
    return random.choice(no_match['responses'])

# Start chat
def start_chat():
    print("ChatBot: Hello! Type 'exit' to end the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("ChatBot: Goodbye!")
            break
        response = get_response(user_input)
        print(f"ChatBot: {response}")

if __name__ == "__main__":
    start_chat()

