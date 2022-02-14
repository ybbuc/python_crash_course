cars = ['bmw', 'audi', 'toyota', 'subaru']

print('Here is the original list:')

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

print('\nHere is the list in reverse order:')
cars.reverse()
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
