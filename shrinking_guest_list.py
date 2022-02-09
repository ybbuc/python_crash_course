guests = ['john', 'jane', 'jim', 'jill']

print("\nI found a bigger table.\n")

guests.insert(0, 'james')
guests.insert(3, 'joe')
guests.append('julie')

print(guests[0].title() + ", you are invited to dinner.")
print(guests[1].title() + ", you are invited to dinner.")
print(guests[2].title() + ", you are invited to dinner.")
print(guests[3].title() + ", you are invited to dinner.")
print(guests[4].title() + ", you are invited to dinner.")
print(guests[5].title() + ", you are invited to dinner.")
print(guests[6].title() + ", you are invited to dinner.")

print("\nI can only invite two people to dinner.\n")

popped_guest = guests.pop()
print(f"Sorry, {popped_guest.title()}, I can't invite you to dinner.")
popped_guest = guests.pop()
print(f"Sorry, {popped_guest.title()}, I can't invite you to dinner.")
popped_guest = guests.pop()
print(f"Sorry, {popped_guest.title()}, I can't invite you to dinner.")
popped_guest = guests.pop()
print(f"Sorry, {popped_guest.title()}, I can't invite you to dinner.")
popped_guest = guests.pop()
print(f"Sorry, {popped_guest.title()}, I can't invite you to dinner.")

print("\n" + guests[0].title() + ", you are still invited to dinner.")
print(guests[1].title() + ", you are still invited to dinner.")

del guests[0]
del guests[0]
print(guests)