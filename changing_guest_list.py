guests = ['john', 'jane', 'jim', 'jill']

busy_guest = guests.pop(1)
print(f"\n{busy_guest.title()} is busy and can't make it to dinner.\n")

guests.insert(1, 'julie')

print(guests[0].title() + ", you are invited to dinner.")
print(guests[1].title() + ", you are invited to dinner.")
print(guests[2].title() + ", you are invited to dinner.")
print(guests[3].title() + ", you are invited to dinner.")