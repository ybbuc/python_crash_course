print("Give me two numbers and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\n First number: ")
    if first_number.lower() == 'q':
        break
    second_number = input("Second number: ")
    if second_number.lower() == 'q':
        break
    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("You must enter numbers!")
    else:
        print("       Answer:", answer)
