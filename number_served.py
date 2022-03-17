class Restaurant:
    """A simple attempt to model a restaurant."""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant (self):
        """Display a short message describing the restaurant."""
        print(f"The name of the restaurant is {self.restaurant_name}.")
        print(f"The type of cuisine is {self.cuisine_type}.")

    def open_restaurant(self):
        """Display a message indicating the restaurant is open."""
        print(f"{self.restaurant_name} is open.")

    def set_number_served(self, number_served):
        """Set the number of customers served a the restaurant."""
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        """Add the given number of customers served to the total."""
        self.number_served += additional_served

restaurant_1 = Restaurant("Zeitgeist", "German")
restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()
print(restaurant_1.number_served)
restaurant_1.number_served += 1
print(restaurant_1.number_served)

print(f"\nNumber served: {restaurant_1.number_served}")
restaurant_1.number_served = 430
print(f"Number served: {restaurant_1.number_served}")

restaurant_1.set_number_served(1257)
print(f"Number served: {restaurant_1.number_served}")

restaurant_1.increment_number_served(239)
print(f"Number served: {restaurant_1.number_served}")
