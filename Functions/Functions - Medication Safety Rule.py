import os
import time

age = 0
weight = 0

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
