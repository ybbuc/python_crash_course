from random import randint

lottery_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "a", "b", "c", "d", "e", "f"]

print("Welcome to the lottery!")
print("Any ticket matching these four numbers or letters wins a prize:")
for i in range(0, 4):
    print(lottery_numbers[randint(0, len(lottery_numbers) - 1)], end=" ")
