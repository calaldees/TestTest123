from random import randint

class Die:
    def __init__(self, sides=6,name="Dicy"):
        self.sides = sides
        self.name = name
    
    def roll(self):
        return randint(1, self.sides)

    def name(self):
        return self.name

    def ChangeSides(self,sides):
        self.sides=sides

    def GetSides(self):
        return self.sides
"""
class DiceBag:
    def __init__(self, sides=[]):
        self.dice = self.create_dice_from_sides(sides)
    
    def create_dice_from_sides(self, sides):
        return list(map(lambda side: Die(side), sides))
    
    def roll_bag(self):
        return list(map(lambda dice: dice.roll(), self.dice))
"""

if __name__ == "__main__":

    die = Die(7,"Steven")
    print(die.roll())

    print("Sides:",die.GetSides())

    die.ChangeSides(8)

    print("Sides",die.GetSides())
