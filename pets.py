pets = {
    'spot': {
        'type': 'dog',
        'owner': 'susan',
    },
    'fluffy': {
        'type': 'cat',
        'owner': 'frank',
    },
    'fins': {
        'type': 'fish',
        'owner': 'jim',
    }
}

for pet in pets:
    print(f"{pets[pet]['owner'].title()} owns a {pets[pet]['type'].title()} named '{pet.title()}'.")


def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
