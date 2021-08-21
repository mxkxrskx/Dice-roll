from random import randint

class Die():
    def __init__(self, nums_sides=6):
        self.num_sides = nums_sides
    def roll(self):
        return randint(1, self.num_sides)
