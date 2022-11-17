def city_country(city, country):
    """Returns a city with its country"""
    city_info = f"{city}, {country}"
    return city_info.title()

info = city_country("maracaibo", "venezuela")
print(info)

info = city_country("bogota", "colombia")
print(info)

info = city_country("toronto", "canada")
print(info)