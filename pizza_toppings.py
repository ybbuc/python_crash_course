toppings = ""
while toppings != 'quit':
    prompt = "\nPlease enter a series of pizza toppings: "
    prompt += "\n(Enter 'quit' when you are finished.) "
    toppings = input(prompt)
    if toppings.lower() == 'quit':
        break
    print("I'll add " + toppings + " to your pizza.")

