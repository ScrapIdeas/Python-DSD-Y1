import os
import time

requiredcheck = True
age = 0
medicalclearance = ""



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