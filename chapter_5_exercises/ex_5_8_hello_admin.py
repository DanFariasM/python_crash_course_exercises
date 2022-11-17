usernames = ["Dan", "MT", "Jose", "Guga", "Admin"]

if usernames:
    for user in usernames:
        if user == "Admin":
            print("Hello Admin!, would you like a status report?")
        else:
            print(f"Hello {user}, thanks you for loggin in again")
else:
    print("We need to find some users!")