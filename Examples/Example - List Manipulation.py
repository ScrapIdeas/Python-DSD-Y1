energy = []
usernames = []
stepcounts = []
list = True
import os
import time
while(list):
    print("Which list would you like to add to?  energy, usernames, stepcounts.")
    r = input("")
    if(r == "energy"):
        if(energy == 4):
            print("You've reached the limit.")
        r2 = int(input(""))
        energy.append(r2)
    if(r == "usernames"):
        if(usernames == 9):
            print("You've reached the limit.")
        usernames.append(r)
    if(r == "stepcounts"):
         if(stepcounts == 6):
             print("You've already reached the limit.")
         r1 = int(input(""))
         stepcounts.append(r1)
    if(energy == 4 & stepcounts == 6 & usernames == 9):
        print("You've reached the total limit.")
        time.sleep(2)
        r = "quit"
    elif(r == "quit"):
        os.system("CLS")
        time.sleep(2)
        print("STEPCOUNTS:")
        print(stepcounts)
        print(stepcounts[-1], stepcounts[0], stepcounts[4])
        time.sleep(2)
        print("ENERGY:")
        print(energy)
        print(energy [-1], energy [2], energy [0])
        time.sleep(2)
        print("USERNAMES:")
        print(usernames)
        print(usernames [-1], usernames [0], usernames [4])
        quit()