from random import randint

class Die:
    """Simulates throwing a die"""

    def __init__(self, sides=6):
        """Initiates the simulation of a die"""
        self.sides = sides

    def roll_die(self, sides=6):
        """Simulates throwing the die"""
        roll = (randint(1,self.sides))
        return roll

results = []

print("Rolling a 6-sided die, 10 times:")
six_sided_die = Die()
for tries in range(0,10):
    result = six_sided_die.roll_die()
    results.append(result)
print(results)

results = []

print("\nRolling a 10-sided die, 10 times:")
ten_sided_die = Die(10)
for tries in range(0,10):
    result = ten_sided_die.roll_die()
    results.append(result)
print(results)

results = []

print("\nRolling a 10-sided die, 10 times:")
twenty_sided_die = Die(20)
for tries in range(0,10):
    result = twenty_sided_die.roll_die()
    results.append(result)
print(results)