class User:
    """Modeling a user"""

    def __init__(self, first_name, last_name, age, country):
        """Initializing user personal information"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country

    def describe_user(self):
        """Describing an user"""
        print(f"This is {self.first_name.title()} {self.last_name.title()}, "
            f"he/she is {self.age} years old, born in {self.country.title()}.")

    def greet_user(self):
        """Greeting the user"""
        print(f"Welcome back {self.first_name.title()}!!")


dan = User("daniel", "farias", 33, "venezuela")
jj = User("jose", "bracho", 34, "canada")

dan.describe_user()
dan.greet_user()

jj.describe_user()
jj.greet_user()