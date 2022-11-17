favorite_places = {
    "daniel": ["toronto", "maracaibo", "aruba"],
    "jose": ["united kingdom", "isla tortuga", "vancouver"],
    "gabf": ["brazil", "argentina", "venezuela"],
    }

for name, places in favorite_places.items():
    print(f"\nI know {name.title()}'s favorite places are:")
    for place in places:
        print(place.title())