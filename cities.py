cities = {
    'new york': {
        'country': 'united states',
        'population': 8406000,
        'fact': 'the city that never sleeps'
    },
    'paris': {
        'country': 'france',
        'population': 2244000,
        'fact': 'the city that never sleeps'
    },
    'tokyo': {
        'country': 'japan',
        'population': 9000000,
        'fact': 'the city that never sleeps'
    },
}

for city in cities:
    print("\n" + city.title())
    print(f"Country: {cities[city]['country'].title()}")
    print(f"Population: {cities[city]['population']}")
    print(f"Fact: {cities[city]['fact']}")

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")
