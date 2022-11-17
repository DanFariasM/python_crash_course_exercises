favorite_numbers = {
    "daniel": [17, 10, 88],
    "mt": [25, 2, 90],
    "jose": [26, 2, 88],
    "guga": [4, 17, 88],
    "jorge": [11, 2, 87],
    }

for name, numbers in favorite_numbers.items():
    print(f"{name.title()}'s favorite numbers are:")
    print(numbers)
    for number in numbers:
        print(number)