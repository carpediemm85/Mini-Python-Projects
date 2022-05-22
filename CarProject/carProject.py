command = input("> ").lower()
started =False
if command == "help":
    print("""
    start - to start car   
    stop - to stop car
    quit - exit and finish.
    """)
while True:
    command = input("> ").lower()
    if command =="start":
        if started:
            print("Car already started...")
        else:
            started =True
            print("Car started...")

    elif command =="stop":
        if not started:
            print("Car already stopped...")
        else:
            started=False
            print("car stopped")
    elif command =="quit":
        break
    else:
        print("I don't understand you...")
    