def greet_users(names):
    """Print a simple greeting to the users on the list"""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)