import os
import time

heartrate = 0
asleep = ""

print("Hello there, asking for base values before activating..")
heartrate = int(input("What is your heartrate?\n"))
if(40 <= heartrate <= 60):
    asleep = True
    print("You're currently asleep.")
if(heartrate != isinstance(int)):
    print("This isn't a string, try again by typing in the function in the menu.")
    time.sleep(3)
    os.system("CLS")
elif(heartrate >= 100):
    print("ALERT: Patient has unusually high BP/M.")
    print("Intervention Needed.")
    time.sleep(3)
    os.system("CLS")
else:
    print("Your heartrate is fine.")
    time.sleep(3)
    os.system("CLS")