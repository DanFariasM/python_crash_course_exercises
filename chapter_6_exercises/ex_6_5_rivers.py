rivers = {
    "amazon": "venezuela",
    "nile": "egypt",
    "mississippi": "usa",
    }

for river, country in rivers.items():
    print(f"The {river.title()} river runs through {country.title()}.")

print("\nThe rivers mentioned are:")
for river in rivers.keys():
    print(river.title())

print("\nThe countries mentioned are:")
for country in rivers.values():
    print(country.title())
