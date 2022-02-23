def greet_user(username):
    """Display a simple greeting"""
    print(f"\nHello, {username}!")

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)

greet_user(name)
