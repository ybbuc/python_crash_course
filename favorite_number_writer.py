"""Prompt for a new favorite number."""

import json

favorite_number = input("What is your favorite number? ")
filename = 'favorite_number.json'
with open(filename, 'w', encoding='utf-8') as f:
    json.dump(favorite_number, f)
