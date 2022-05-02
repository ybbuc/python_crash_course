name = input("Name: ")
print(f"Hello {name}!")

filename = "guest.txt"

with open(filename, 'w') as file_object:
    file_object.write(name)
