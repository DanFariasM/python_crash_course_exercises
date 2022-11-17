class Employee:
    """Models a new employee."""

    def __init__(self, first_name, last_name, salary):
        """Keep new employee's information."""
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, add_raise=5000):
        """give the desired salary raise to the employee."""
        self.salary += add_raise


