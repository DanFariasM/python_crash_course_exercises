seats = input("How many people are in your dinner group? ")
seats = int(seats)

if seats > 8:
    print("Sorry, you need to wait for a table.")
else:
    print(f"Your table for {seats} is ready.")