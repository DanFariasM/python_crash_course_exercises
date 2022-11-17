import json

filename = "favorite_number.json"

with open(filename, "w") as f:
    number = input("What is your favorite number? ")
    json.dump(number, f)
    print("We will remember your favorite number when you come back!")
