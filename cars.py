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

def make_car(manufacturer, model, **car_info):
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
