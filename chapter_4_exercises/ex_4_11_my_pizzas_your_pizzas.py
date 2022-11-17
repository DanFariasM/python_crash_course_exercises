pizzas = ["veggie", "canadian", "4 cheese"]
friend_pizzas = pizzas[:]
print(pizzas)
pizzas.append("deluxe")
friend_pizzas.append("platanera")
print("\nMy favorite pizzas are:")
for pizza in pizzas:
	print(pizza)
print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
	print(pizza)
	