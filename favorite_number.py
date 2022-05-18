import json

def get_stored_favorite_number():
    """Get stored favorite number if available."""
    filename = 'favorite_number.json'
    try:
        with open(filename, encoding='utf-8') as f:
            favorite_number = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return favorite_number

def get_new_favorite_number():
    """Prompt for a new favorite number."""
    favorite_number = input("What is your favorite number? ")
    filename = 'favorite_number.json'
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(favorite_number, f)
    return favorite_number

def reveal_favorite_number():
    """Reveal the user's favorite number."""
    favorite_number = get_stored_favorite_number()
    if favorite_number:
        print(f"I know your favorite number! It's {favorite_number}.")
    else:
        favorite_number = get_new_favorite_number()
        print(f"I'll remember your favorite number, {favorite_number}!")

reveal_favorite_number()
