import random

dice1 = 0
dice2 = 0


def roll():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    print("First dice rolled was a " + str(dice1))
    print("Second dice rolled was a " + str(dice2))
    print("Together these total " + str(dice1 + dice2))


roll()
