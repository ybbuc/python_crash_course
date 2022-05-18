import json

filename = 'favorite_number.json'
try:
    with open(filename, encoding='utf-8') as f:
        favorite_number = json.load(f)
except FileNotFoundError:
    favorite_number = input("What is your favorite number? ")
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(favorite_number, f)
    print(f"I'll remember your favorite number, {favorite_number}!")
else:
    print(f"I know your favorite number! It's {favorite_number}.")

