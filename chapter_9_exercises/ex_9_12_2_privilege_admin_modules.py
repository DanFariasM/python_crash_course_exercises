from ex_9_12_1_user_module import User

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