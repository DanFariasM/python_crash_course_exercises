def describe_city(city, country="venezuela"):
    """Information about a city"""
    print(f"{city.title()} is in {country.title()}.")

describe_city("maracaibo")
describe_city("caracas")
describe_city("toronto", "canada")