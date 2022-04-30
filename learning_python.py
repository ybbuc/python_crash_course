filename = 'learning_python.txt'

# Print the contents once by reading in the entire file
with open(filename) as file_object:
    contents = file_object.read()
print(contents)

# Print the contents by looping over the file object
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

# Print the contents by storing the lines in a list and working with them
# outside the 'with' block
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
