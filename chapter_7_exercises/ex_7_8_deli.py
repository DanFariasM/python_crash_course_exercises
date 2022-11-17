sandwich_orders = ["jam", "cheese", "club", "egg and bacon"]
finished_sandwiches = []

while sandwich_orders:
    order = sandwich_orders.pop()
    print(f"I made your {order} sandwich!")
    finished_sandwiches.append(order)

print("\nSandiwches ready:")
for dish in finished_sandwiches:
    print(f"Your {dish} sandwich is ready!")

