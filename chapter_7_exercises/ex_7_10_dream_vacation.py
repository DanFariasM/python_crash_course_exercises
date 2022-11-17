dream_vacation = {}

prompt = "If you could go to any place in the world, "
prompt += "where would you go? "

while True:

    name = input("\nWhat is your name? ")
    place = input(prompt)

    dream_vacation[name] = place

    active = input("Do you want to ask another person? (yes/no) ")
    if active == "no":
        break

print("\n--- Results of the poll ---")

for name, place in dream_vacation.items():
    print(f"{name.title()} would love to go to {place.title()}")

