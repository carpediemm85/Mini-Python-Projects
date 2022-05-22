import random
import re 
from secrets import choice

while True:
    print("\n")
    print("------Rock Paper Scissors ------")
    userChoice = input("Choose your weapon : [R]ock, [P]aper, [S]cissors !  >>> ")
    if not re.match("[SsRrPp]", userChoice):
        print ("Please choose a letter:")
        print ("[R]ock, [S]cissors or [P]aper.")
        continue
    print("\n") 
    print("Your choise: " + userChoice)
    choices = ("P", "R", "S")
    opponentChoice =random.choice(choices)
    print("I chose: " + opponentChoice)

    if opponentChoice == userChoice:
        print("Thie! ")

    elif opponentChoice == 'R' and userChoice == 'S':
        print ("Scissors beats rock, I win! ")
        continue
    elif opponentChoice == 'S' and userChoice.upper() == 'P':      
        print ("Scissors beats paper! I win! ")
        continue
    elif opponentChoice == 'P' and userChoice.upper() == 'R':      
        print ("Paper beat rock,      I win! ")
        continue
    else:       
        print ("----You win!----")
