favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
    }

people_to_poll = ["jen", "jose", "sarah", "edward", "daniel", "phil"]

for name in people_to_poll:
    if name in favorite_languages.keys():
        print(f"Thank you {name.title()} for taking the poll!")
    else:
        print(f"{name.title()}, please take the poll.")