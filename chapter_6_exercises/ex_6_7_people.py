person_1 = {
    "first_name": "daniel",
    "last_name": "farias",
    "age": 33,
    "city": "maracaibo",
    }

person_2 = {
    "first_name": "jose",
    "last_name": "bracho",
    "age": 34,
    "city": "la lago",
    }

person_3 = {
    "first_name": "maria",
    "last_name": "chacin",
    "age": 32,
    "city": "sabaneta",
    }

people = [person_1, person_2, person_3]

for person in people:
    print(person)

for person in people:
    print(f"\nFull name: {person['first_name'].title()} {person['last_name'].title()}")
    print(f"Age: {person['age']}")
    print(f"Born in: {person['city'].title()}")

