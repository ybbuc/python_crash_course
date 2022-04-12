from random import randint

class Die:
    """A simple attempt to model a die."""
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        """Return a random number between 1 and number of sides."""
        return randint(1, self.sides)

die_6 = Die(6)
die_10 = Die(10)
die_20 = Die(20)

for roll_num in range(1, 11):
    print(f"Roll #{roll_num}: {die_6.roll_die()}")

for roll_num in range(1, 11):
    print(f"Roll #{roll_num}: {die_10.roll_die()}")

for roll_num in range(1, 11):
    print(f"Roll #{roll_num}: {die_20.roll_die()}")
