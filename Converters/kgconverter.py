weight = int(input("How much are kg? "))
unit = input("Kg(K) or lbs(L)? ")

if unit.upper() == "K":
    converted = weight/0.45
    print(f"You are {round(converted)} pounds")
else:
    converted = weight*0.45
    print(f"You are {converted} kilos")

