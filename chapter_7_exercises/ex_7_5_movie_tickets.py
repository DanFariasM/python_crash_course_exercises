prompt = "\nPlease tell us your age for your ticket price."
prompt += "\nEnter 'quit' to exit. "

while True:
    age = input(prompt)

    if age == "quit":
        break
    else:
        age = int(age)
        if age < 3:
            cost = "free!"
        elif age <= 12:
            cost = "$10"
        else:
            cost = "$15"
        print(f"Your ticket is {cost}")
