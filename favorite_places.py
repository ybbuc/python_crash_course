favorite_places = {
    'james': ['paris', 'london', 'new york'],
    'joe': ['berlin', 'los angeles', 'new york'],
    'jane': ['paris', 'london', 'new york'],
}

for name, places in favorite_places.items():
    print("\n" + name.title() + "'s favorite places are:")
    for place in places:
        print("\t" + place.title())
