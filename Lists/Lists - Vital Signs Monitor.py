import time
import os
temp = 0
oxygen = 0
heartrate = 0
Results = {} #Went unused since I can't append in functions as of right now.
MENULOOP = True
FUNCTIONSAVAILABLE = {"[1] VitalSigns","[2] OxygenLevel","[3] HeartRate"}
def VitalSigns():
    temp = input("I'd like to ask you for the temperature.")
    if(temp != isinstance(temp, int)):
        print("This isn't a integer.")
        print("Backing out to prevent Err.")
        time.sleep(3)
        os.system("cls")
    elif(temp > 37.5):
        print("Uh-oh! High-Temperature Warning!")
    else:
        print(f"Your temperature is: {temp}")
def OxygenLevel():
    oxygen = input("Input your estimated oxygen level.")
    if(oxygen != isinstance(oxygen, int)):
        print("This isn't a integer.")
        print("Backing out to prevent Err.")
        time.sleep(3)
        os.system("cls")
    elif(oxygen < 92):
        print("Low Oxygen Level, Rapidly decreasing.")
    else:
        print(f"Your Current Oxygen Level: {oxygen}")
def HeartRate():
    heartrate = input("I'd llike to ask you for the approximate BP/M you have.")
    if(heartrate != isinstance(heartrate, int)):
        print("This isn't an integer.")
        print("Backing out to prevent Err.")
        time.sleep(3)
        os.system("cls")
    elif(60 <= heartrate <= 100):
        print("Heartrate Normal, please proceed.")
    elif(90 <= heartrate <= 150):
        print("Heartrate escalating to unstable levels, please seek medical help.")
    else:
        print(f"Your approximate BPM: {heartrate}")

while(MENULOOP == True):
    print("Welcome to the Vital Signs Monitor.exe")
    print("Which function would you like to access?")
    print(FUNCTIONSAVAILABLE)
    print("Type in 'Quit' to exit the program.")
    response1 = input("")
    if(response1 == "VitalSigns"):
        VitalSigns()
    if(response1 == "OxygenLevel"):
        OxygenLevel()
    if(response1 == "HeartRate"):
        HeartRate()
    if(response1 == "Quit"):
        time.sleep(1)
        print(f"Your Temperature: {temp}")
        time.sleep(1)
        print(f"Your Oxygen: {oxygen}")
        time.sleep(1)
        print(f"Your Heart Rate: {heartrate}")
        time.sleep(5)
        exit(0)