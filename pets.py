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
