filename = "programming_poll.txt"

with open(filename, 'w') as file_object:
    response = ''
    while response.lower() != 'quit':
        print("\nEnter \"quit\" to exit the program.")
        response = input("Why do you like programming? ")
        if response.lower() != 'quit':
            file_object.write(response + "\n")
