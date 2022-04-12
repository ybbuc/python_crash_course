from mimetypes import init


class Restaurant:
    """A simple attempt to model a restaurant."""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant (self):
        """Display a short message describing the restaurant."""
        print(f"The name of the restaurant is {self.restaurant_name}.")
        print(f"The type of cuisine is {self.cuisine_type}.")

    def open_restaurant(self):
        """Display a message indicating the restaurant is open."""
        print(f"{self.restaurant_name} is open.")
