my_pizzas = ['pepperoni', 'sausage', 'cheese', 'veggie']
your_pizzas = my_pizzas[:]

my_pizzas.append('pineapple')
your_pizzas.append('mediterranean')

print('My favorite pizzas are:')

for pizza in my_pizzas:
    print(pizza)

print('\nMy friend\'s favorite pizzas are:')

for pizza in your_pizzas:
    print(pizza)