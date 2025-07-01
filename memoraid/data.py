import os
import json

DATA_FILE = "memoraid.json"

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"decks": []}
    
    with open(DATA_FILE, "r") as file:
        return json.load(file)