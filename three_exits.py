active = True
while active is True:
    prompt = "\nPlease enter a series of pizza toppings: "
    prompt += "\n(Enter 'quit' when you are finished.) "
    toppings = input(prompt)
    if toppings.lower() == 'quit':
        active = False
        break
    print("I'll add " + toppings + " to your pizza.")
