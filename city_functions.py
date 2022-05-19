def get_formatted_city_name(city, country, population=''):
    """Generate a neatly formatted city name.."""
    if population:
        full_name = f"{city.title()}, {country.title()} - population {population}"
    else:
        full_name = f"{city.title()}, {country.title()}"
    return full_name
