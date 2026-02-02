age = 0
lowincome = False
dayssincelasttime = 0
eligibleforfreeclass = False
age = int(input("Hello, What's your age!"))
r = str(input("Hello there, are you from a low income family?"))
if(r == "Yes"):
    lowincome = True
else:
    lowincome = False
dayssincelasttime = int(input("And lastly, how many days has it been since the last time you've visited?"))

if(16 <= age >= 25 & lowincome == True):
    if(dayssincelasttime >= 30):
        print("Unfortunately, you're not eligible for a free class.")
    print("You're eligible for a free class!")
    eligibleforfreeclass = True
    print(f"{eligibleforfreeclass}")
