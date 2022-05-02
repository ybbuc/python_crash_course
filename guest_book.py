filename = "guest_book.txt"

with open(filename, 'w') as file_object:
    name = ''
    while name.lower() != 'quit':
        print("\nEnter \"quit\" to exit the program.")
        name = input("Name: ")
        if name.lower() != 'quit':
            print(f"Welcome {name}!")
            file_object.write(name + "\n")
