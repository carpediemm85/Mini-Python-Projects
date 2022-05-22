import random


choice = input("""---Hello, please enter your choice: 
for 

Range of 1-10(a);
Range of 10-100(b);
Range of 100-1000(c);
Own range(d);
(Please type the letter in parentheses for selection.)

>>> """)

if choice == "a":
    guessNum = random.randint(1,10)
    questGuess = int(input("""Okay i choosed randomly an integer. Now tell me your guess>>> """))
    if questGuess == guessNum:
        print("You rock!")
    else:
        print("Unfortunately you lost")

elif choice == "b":
    guessNum = random.randint(10,100)
    questGuess = int(input("""Okay i choosed randomly an integer. Now tell me your guess>>> """))
    if questGuess == guessNum:
        print("You rock!")
    else:
        print("Unfortunately you lost")

elif choice == "c":
    guessNum = random.randint(100,1000)
    questGuess = int(input("""Okay i choosed randomly an integer. Now tell me your guess>>> """))
    if questGuess == guessNum:
        print("You rock!")
    else:
        print("Unfortunately you lost")

elif choice == "d":
    a = int(input("Please enter minimum of your range>>> "))
    b = int(input("Please enter maximum of your range>>> "))
    
    guessNum = random.randint(a,b)
    questGuess = int(input("""Okay i choosed randomly an integer. Now tell me your guess>>> """))
    if questGuess == guessNum:
        print("You rock!")
    else:
        print("Unfortunately you lost")

else:
    print("I don't understand you.Please run again...")