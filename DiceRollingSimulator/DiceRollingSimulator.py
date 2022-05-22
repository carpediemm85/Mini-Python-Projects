from ast import Return
import random

while True:
    def Rand():
        return random.randint(1,6)


    a = Rand()
    b = Rand()
    Dice = [a,b]

    print(Dice)

    choose = input("Do you want Roll the dice again? Y/N >> ").lower()
    if choose != "y":
        break