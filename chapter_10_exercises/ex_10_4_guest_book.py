filename = "guest_book.txt"

with open(filename, "w") as file_object:
    file_object.write("Guest names:\n")
    while True:
        print("Please enter 'q' at any time to quit.")
        guest = input("Please enter your name: ")
        if guest == "q":
            break
        else:
            print(f"Hello {guest}! Your visit has been logged.\n")
            file_object.write(f"{guest}\n")