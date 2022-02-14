pizzas = ['pepperoni', 'sausage', 'cheese', 'veggie', 'pineapple']
for pizza in pizzas:
    print(f"I like {pizza} pizza.")

print("\nI really love pizza!")

print('The first three items in the list are:')

for pizza in pizzas[:3]:
    print(pizza)

print('Three items from the middle of the list are:')

for pizza in pizzas[1:4]:
    print(pizza)

print('The last three items in the list are:')

for pizza in pizzas[-3:]:
    print(pizza)