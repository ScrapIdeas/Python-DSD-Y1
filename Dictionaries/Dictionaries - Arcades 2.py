#One or two functions are unfinished, sorry kye.


import time
import os
machines  = ["Pinball Wizard", "Dance Floor X", "Retro Racer", "Alien Blaster"] 
categories = ["Pinball", " Rhythm", "   Racing", " Shooter"] 
status     = ["Working", " Working", "   Needs Service", " Working"] 
r = ""
filteringbycategory = False
machinesavailable = 4
availablefunctions = ["View Machines", "Register New Machine", "Update Status", "List Machines needing service - Inoperational for now."]
machinescategories = {
    machines[0]:categories[0],
    machines[1]:categories[1],
    machines[2]:categories[2],
    machines[3]:categories[3],
}
machinesandstatus = {
    machines[0] : status[0],
    machines[1] : status[1],
    machines[2] : status[2],
    machines[3] : status[3],
}
def viewmachines():
    global filteringbycategory #Sorry kye, need to make this global otherwise I'm genuinely gonna get another headache.
    r = input("Which one would you like to View? Status / Machines / Settings\n")
    if(r == "Machines"):
        print("Names                Categories")
        for x in machinescategories:
            print(f"{x}         {machinescategories[x]}")
        if(filteringbycategory == True):
            print("This is a work in progress, might not be finished.")
            os.system("CLS")
            time.sleep(2)
            filteringbycategory = False

    if(r == "Settings"):
        print("There's only one setting here, and its filtering by category.")
        print("Would you like to turn it on?")
        r = input("")
        if(r == "Yes"):
            filteringbycategory = True
        else:
            filteringbycategory = False

    elif(r == "Status"):
        print("Names                 Status")
        for x in machinesandstatus:
            print(f"{x}          {machinesandstatus[x]}")
        time.sleep(2)
        os.system("CLS")
def appendmachines():
    time.sleep(1)
    r = input("List your machine here.\n")
    machines.append(r)
    time.sleep(1)
    r = input("What is its category?\n")
    categories.append(r)
    time.sleep(1)
    r = input("And its status?\n")
    status.append(r)
    print("Everything successfully added, review it in the View Machines function.")
    machines+=1
def updatestatus():
    print(f"Which machine would you like to update the status of? (1 <--> {machinesavailable})")
    for x in machinesandstatus:
        print(x, machinesandstatus[x])
    r = input()
    print(machines(r))
    r = input("What is its status?")
       t = input(f"And the column? 1 - {machinesavailable} ")
        r = status.pop(t)
        print("Status successfully changed, check it out in the View Machines Option.")





print("Welcome to the Arcade & Snackbar Operational Suite!")
print("Which function would you like to access?")
print(availablefunctions)
r = input()
if(r == "View Machines"):
    viewmachines()
elif(r == "Register New Machine"):
    appendmachines()
elif(r == "Update Status"):
    updatestatus()