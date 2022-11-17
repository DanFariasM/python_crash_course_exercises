import json

filename = "favorite_number_remembered.json"

try:
    with open(filename) as f:
        number = json.load(f)
except FileNotFoundError:
    with open(filename, "w") as f:
        number = input("What is your favorite number? ")
        json.dump(number, f)
        print("We will remember your favorite number when you come back!")
else:
    print(f"I know you favorite number, it's {number}!")