def make_sandwich(*ingredients):
    """List the ingredients for a sandwich"""
    print("\nCreating a sanwich with the following ingredients:")
    for ingredient in ingredients:
        print(f"- {ingredient}")


make_sandwich("ham")
make_sandwich("cheese", "tomato", "onion")
make_sandwich("lettuce", "mushrooms")
