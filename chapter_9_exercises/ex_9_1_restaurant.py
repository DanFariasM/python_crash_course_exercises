class Restaurant:
    """Modeling a restaurant place"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Gives a description of the restaurant"""
        print(f"The restaurant {self.restaurant_name.title()} "
            f"serves {self.cuisine_type} food.")

    def open_restaurant(self):
        """Creates a message saying the restaurant is open"""
        print(f"The restaurant {self.restaurant_name.title()} is now open.")


restaurant = Restaurant("franco", "junk")

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()