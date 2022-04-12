class User:
    """A simple attempt to model a user."""
    def __init__(self, first_name, last_name):
        """Initialize first name and last name attributes."""
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        """Display a short message describing the user."""
        print(f"Name: {self.first_name} {self.last_name}")

    def greet_user(self):
        """Display a personalized message greeting the user."""
        print(f"Welcome, {self.first_name}!")
