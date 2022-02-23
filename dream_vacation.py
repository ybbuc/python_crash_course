prompt = "\nIf you could visit one place in the world, where would you go?"
prompt += "\n Enter 'quit' to exit: "

places = []
flag = True

while flag:
    poll = input(prompt)
    if poll.lower() == 'quit':
        flag = False
    elif poll.strip() != '': # Ignore empty input
        places.append(poll)

print("\nPlaces you'd like to go:")
for place in places:
    print(place)
