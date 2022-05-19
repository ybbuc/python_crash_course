from city_functions import get_formatted_city_name

print("Enter 'q' at any time to quit.")
while True:
    city = input("\nPlease give me a city name: ")
    if city.lower() == 'q':
        break
    country = input("Please give me a country name: ")
    if country.lower() == 'q':
        break
    population = input("Please give me the population: ")
    if country.lower() == 'q':
        break

    formatted_city_name = get_formatted_city_name(city, country, population)
    print(f"\nNeatly formatted: {formatted_city_name}")
