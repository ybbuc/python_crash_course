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

restaurant_1 = Restaurant("Zeitgeist", "German")
print(f"\nRestaurant name: {restaurant_1.restaurant_name}")
print(f"Cuisine type: {restaurant_1.cuisine_type}")
restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()

restaurant_2 = Restaurant("Currify", "Indian")
print(f"\nRestaurant name: {restaurant_2.restaurant_name}")
print(f"Cuisine type: {restaurant_2.cuisine_type}")
restaurant_2.describe_restaurant()
restaurant_2.open_restaurant()

restaurant_3 = Restaurant("Charlie's", "American")
print(f"\nRestaurant name: {restaurant_3.restaurant_name}")
print(f"Cuisine type: {restaurant_3.cuisine_type}")
restaurant_3.describe_restaurant()
restaurant_3.open_restaurant()
