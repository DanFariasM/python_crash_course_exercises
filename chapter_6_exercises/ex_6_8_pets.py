pet_1 = {
    "type of pet": "dog",
    "name": "moty",
    "owner": "victor",
    }

pet_2 = {
    "type of pet": "cat",
    "name": "luna",
    "owner": "mt",    
    }

pet_3 = {
    "type of pet": "bird",
    "name": "piolin",
    "owner": "igua",
    }

pets = [pet_1, pet_2, pet_3]

for pet in pets:
    print(pet)

for pet in pets:
    print(f"\nThis is what I know about {pet['name'].title()}:")
    for key, value in pet.items():
        print(f"{key.title()}: {value.title()}")
