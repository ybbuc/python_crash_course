people = {
    'Guido': {
        'first_name': 'Guido',
        'last_name': 'van Rossum',
        'age': 56,
        'city': 'Montreal'
    },
    'Alice': {
        'first_name': 'Alice',
        'last_name': 'Wonderland',
        'age': 20,
        'city': 'London',
    },
    'Bob': {
        'first_name': 'Bob',
        'last_name': 'Smith',
        'age': 30,
        'city': 'New York',
    },

}

for person in people:
    print(f"\nFirst name: {people[person]['first_name']}")
    print(f"Last name: {people[person]['last_name']}")
    print(f"Age: {people[person]['age']}")
    print(f"City: {people[person]['city']}")
