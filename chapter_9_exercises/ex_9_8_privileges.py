class User:
    """Modeling a user"""

    def __init__(self, first_name, last_name, age, country):
        """Initializing user personal information"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        self.login_attempts = 0

    def describe_user(self):
        """Describing an user"""
        print(f"This is {self.first_name.title()} {self.last_name.title()}, "
            f"he/she is {self.age} years old, born in {self.country.title()}.")

    def greet_user(self):
        """Greeting the user"""
        print(f"Welcome back {self.first_name.title()}!!")

    def increment_login_attempts(self):
        """Increments the value of login attempts by 1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Resets the login attempts"""
        self.login_attempts = 0


class Privileges:
    """Represents the privileges of an Admin"""
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        """Shows a list of admin privileges"""
        print("Admin privileges are:\n")
        for privilege in self.privileges:
            print(f"- {privilege}")

class Admin(User):
    """Representation of an administrator"""

    def __init__(self, first_name, last_name, age, country):
        """Initializing admin information"""
        super().__init__(first_name, last_name, age, country)
        self.privileges = Privileges()


dan_admin = Admin("Daniel", "Farias", 33, "Venezuela")

dan_admin.describe_user()

dan_admin.privileges.show_privileges()