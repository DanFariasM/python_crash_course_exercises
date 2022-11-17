sandwich_orders = ["jam", "pastrami", "cheese", "pastrami",
    "club", "pastrami", "egg and bacon"]
finished_sandwiches = []

print("Sorry, we ran out of pastrami\n")

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    order = sandwich_orders.pop()
    print(f"I made your {order} sandwich!")
    finished_sandwiches.append(order)

print("\nSandiwches ready:")
for dish in finished_sandwiches:
    print(f"Your {dish} sandwich is ready!")


