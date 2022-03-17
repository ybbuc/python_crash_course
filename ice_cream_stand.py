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

class IceCreamStand(Restaurant):
    """Represent aspects of a restaurant, specific to an ice cream stand."""

    def __init__(self, restaurant_name, cuisine_type='ice_cream'):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an ice cream stand.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def describe_flavors(self):
        """Display a message indicating the flavors available."""
        print("Flavors available:")
        for flavor in self.flavors:
            print(f"- {flavor}")

dairy_queen = IceCreamStand("Dairy Queen")
dairy_queen.flavors = ["vanilla", "chocolate", "oreo"]
dairy_queen.describe_flavors()
