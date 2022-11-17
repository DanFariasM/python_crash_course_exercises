def city_country(city,country, population=""):
    """Returns a formated city and country names."""
    if population:
        location = f"{city}, {country} - population {population}"
    else:
        location = f"{city}, {country}"
    return location.title()

