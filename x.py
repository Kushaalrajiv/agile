rr=""
started=False
while True:
    rr=input("> ")
    if rr=="help":
        print('''
    start-to start the car
    stop-to stop the car
    quit-to exit
    ''')
    elif rr=="start":
        if started==False:
            
            print("car started...ready to go")
            started=True
        else:
            print("Car already started")
    elif rr=="stop":
        if started==True:
            print("car stopped")
            started=False
        else:
            print("already stopped")
    elif rr=="quit":
        break

    else:
        print("sorry i dont understand that")

