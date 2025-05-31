import json
import random

def load_random_fact(file_path):
    with open(file_path, 'r') as file:
        facts = json.load(file)
        if not facts:
            print("No facts found.")
            return
        random_fact = random.choice(facts)
        print(json.dumps(random_fact, indent=4))

# Call the function with the path to your facts.json
load_random_fact("facts.json")
