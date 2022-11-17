filename = "programming_poll.txt"

with open(filename, "a") as file_object:
    file_object.write("New poll entry:\nWhat do you like about programming?\n")
    while True:
        print("Please enter 'q' at any time to quit.")
        answer = input("What do you like about programming? ")
        if answer == "q":
            break
        else:
            print("Your answer has been stored.\n")
            file_object.write(f"{answer}\n")