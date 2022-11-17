class Restaurant:
    """Modeling a restaurant place"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Gives a description of the restaurant"""
        print(f"The restaurant {self.restaurant_name.title()} "
            f"serves {self.cuisine_type} food.")

    def open_restaurant(self):
        """Creates a message saying the restaurant is open"""
        print(f"The restaurant {self.restaurant_name.title()} is now open.")

    def set_number_served(self, number_served):
        """Sets the amount of people the restaurant has served"""
        self.number_served = number_served

    def increment_number_served(self, increment):
        """Sets the increment of people served"""
        self.number_served += increment
