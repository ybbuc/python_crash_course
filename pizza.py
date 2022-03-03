def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size} cm pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza(32, 'pepperoni')
make_pizza(24, 'mushrooms', 'green peppers', 'extra cheese')
