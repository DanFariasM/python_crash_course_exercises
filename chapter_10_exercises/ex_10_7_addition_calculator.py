print("Give the program two numbers to add")
print("enter 'q' to quit")

while True:
    first_number = input("\nFirst number: ")
    if first_number == "q":
        break
    second_number = input("\nSecond number: ")
    if second_number == "q":
        break
    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("You can't enter text!")
    else:
        print(answer)