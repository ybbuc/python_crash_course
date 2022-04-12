from user import User

class Privileges:
    """A simple attempt to model the privleges of a user."""
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("Privileges available:")
        for privilege in self.privileges:
            print(f"- {privilege}")


class Admin(User, Privileges):
    """A simple attempt to model an admin user."""

    def __init__(self, first_name, last_name):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an admin.
        """
        super().__init__(first_name, last_name)
        self.privileges = Privileges()
