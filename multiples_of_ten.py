num = int(input('Enter a number: '))

if num % 10 == 0:
    print(f"{num} is a multiple of 10: {num // 10}")
else:
    print(f'{num} is not a multiple of 10')
