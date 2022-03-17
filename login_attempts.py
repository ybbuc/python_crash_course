class User:
    """A simple attempt to model a user."""
    def __init__(self, first_name, last_name):
        """Initialize first name and last name attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        """Display a short message describing the user."""
        print(f"Name: {self.first_name} {self.last_name}")

    def greet_user(self):
        """Display a personalized message greeting the user."""
        print(f"Welcome, {self.first_name}!")

    def increment_login_attempts(self):
        """Increment the value of login_attempts."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset the value of login_attempts to 0."""
        self.login_attempts = 0

user = User("John", "Doe")
user.describe_user()
user.greet_user()
print(f"Login attempts: {user.login_attempts}")
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(f"Login attempts: {user.login_attempts}")
user.reset_login_attempts()
print(f"Login attempts: {user.login_attempts}")
