cities = {
    "maracaibo": {
        "country": "venezuela",
        "population": "4m",
        "fact": "la tierra del sol amada",
        },
    "toronto": {
        "country": "canada",
        "population": "3m",
        "fact": "my new home",
        },
    "hawaii": {
        "country": "US",
        "population": "1m",
        "fact": "a fun island",
        },
    }

for city, info in cities.items():
    print(f"\nHere's some facts about {city.title()}:")
    print(f"It is located in {info['country'].title()},"
        f"it has a population of {info['population']} people"
        f" and it is called {info['fact']}.")