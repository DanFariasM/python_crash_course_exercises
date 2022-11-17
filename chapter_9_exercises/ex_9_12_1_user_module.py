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
