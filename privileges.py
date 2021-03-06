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

class Privileges:
    """A simple attempt to model the privileges of an admin user."""
    def __init__(self):
        """Initialize the privilege's attrributes."""
        self.privileges = ["can add post", "can delete post", "can ban user"]
    def show_privileges(self):
        """Print the list of privileges available to a user."""
        print("Privileges available:")
        for privilege in self.privileges:
            print(f"- {privilege}")

class Admin(User):
    """A simple attempt to model an admin user."""

    def __init__(self, first_name, last_name):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an admin.
        """
        super().__init__(first_name, last_name)
        self.privileges = Privileges()

admin = Admin("John", "Doe")
admin.privileges.show_privileges()
