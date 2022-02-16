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
