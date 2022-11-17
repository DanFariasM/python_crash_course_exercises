filename = "guest.txt"

with open(filename, "w") as file_object:
    file_object.write("Guest name:\n")
    guest = input("Please enter your name: ")
    file_object.write(guest)