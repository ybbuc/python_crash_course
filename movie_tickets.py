age = ""
while age != 'quit':
    prompt = "\nPlease enter your age: "
    prompt += "\n(Enter 'quit' when you are finished.) "
    age = input(prompt)
    if age.lower() == 'quit':
        break
    elif int(age) < 3:
        print("Your ticket is free!")
    elif int(age) < 12:
        print("Your ticket is $10.")
    else:
        print("Your ticket is $15.")
