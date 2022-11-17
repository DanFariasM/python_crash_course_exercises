car = "subaru"
print("Is car == 'subaru'? I predict True.")
print(car == "subaru")

print("\nIs car == 'audi'? I predict False.")
print(car == "audi")

print("\nIs car != 'toyota'? I predict True.")
print(car != "toyota")

car = "Honda"
print("\nIs car == 'honda'? I predict False.")
print(car == "honda")


print("\nIs car.lower() == 'honda'? I predict True.")
print(car.lower() == "honda")

number = 10
print("\nIs number < 4? I predict False.")
print(number < 4)

print("\nIs number >= 9? I predict True.")
print(number >= 9)

number_2 = 15
print("\nIs 12 between number and number_2? I predict True.")
print(number <= 12 and number_2 >=12)

print("\nIs 2 greater than any of the numbers? I predict False.")
print(number < 4 or number_2 < 4)

prinary_colors = ["red", "blue", "yellow"]

print("\nIs red a primary color? I predict True.")
print("red" in prinary_colors)

print("\nIs orange a primary color? I predict False.")
print("orange" in prinary_colors)

print("\nIs purple a secondary color? I predict True.")
print("orange" not in prinary_colors)