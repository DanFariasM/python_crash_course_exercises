current_users = ["Dan", "MT", "Jose", "Guga", "Admin"]

new_users = ["Admin", "jorge", "maria", "juan", "jose"]

current_users_lower = []

for current_user in current_users:
    current_users_lower.append(current_user.lower())

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"{new_user}, please enter a new username")
    else:
        print(f"{new_user}, your username is available")
