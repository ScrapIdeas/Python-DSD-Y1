import os
import time

age = 0
weight = 0
medicalclearance = ""
functions = ("MedicationSafetyRule", "FitnessCentreAccess", "SleepTrackerAlert")
asleep = False
requiredcheck = True
menu = True
heartrate = 0

def MedicationSafetyRule():
    print("Hello there, please enter your age for a brief age check!")
    age = int(input("What is your age?\n"))
    print("Now enter your weight.")
    weight = int(input("What is your weight?\n"))
    if(age >= 12 and weight >= 40):
        print("Safe to give.")
        time.sleep(3)
        os.system("CLS")
    else:
        print("Not safe.")
        time.sleep(3)
        os.system("CLS")

def FitnessCentreAccess():
    print("Hey there, fella. ALlow me to ask for your age.")
    while(requiredcheck == True):
        age = int(input("What is your age?\n"))
        if(age != isinstance(int)):
            print("This isn't a valid age number, try again in the menu.")
            time.sleep(3)
            os.system("CLS")
        print("And do you have any medical clearance?")
        medicalclearance = str(input("Your medical clearance.\n"))
        if(medicalclearance != isinstance(str)):
            print("Do you have the clearance or not? Don't say random numbers.")
            time.sleep(3)
            os.system("CLS")
        if(age >= 18 or medicalclearance == "Recieved"):
            print("Access granted.")
            time.sleep(3)
            os.system("CLS")
            break
        elif(age < 18 or medicalclearance != "Recieved"):
            print("Access Denied.")
            time.sleep(3)
            os.system("CLS")
            break

def SleepTrackerAlert():
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

while(menu == True):
    print("Welcome to the menu, here are our available functions!")
    print(functions)
    r = input("Tell me which one you'd want to use!\n")
    if(r == "MedicationSafetyRule"):
        MedicationSafetyRule()
        time.sleep(6)
        os.system("CLS")
    if(r == "FitnessCentreAccess"):
        FitnessCentreAccess()
        time.sleep(6)
        os.system("CLS")
    if(r == "SleepTrackerAlert"):
        SleepTrackerAlert()
        time.sleep(6)
        os.system("CLS")
    if(r == "Quit"):
        exit(0)
    elif(r != "MedicationSafetyRule" or "FitnessCentreAccess" or "SleepTrackerAlert"):
        print("That isn't one of our functions, type in one of the functions or type in QUIT to quit.")
        time.sleep(3)
        os.system("CLS")
    

