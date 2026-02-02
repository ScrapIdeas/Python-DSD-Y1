Available = ["View","Add","Update","Delete"]
AvailableGenres = ["Pinball","Rhythm","Racing","Shooter"]
Arcade = {
    "Pinball Wizard": {
        "Category" : "Pinball",
        "Status" : "Working",
    },
    "Dance Floor X": {
        "Category" : "Rhythm",
        "Status" : "Working",
    },
    "Retro Racer" : {
        "Category" : "Racing",
        "Status" : "Needs Service",
    },
    "Alien Blaster" : {
        "Category" : "Shooter",
        "Status" : "Working",
    }
}
def ViewingMachines(): #Works because I didn't waste my time trying to do it by user selection.
    r = input("")
    if(r == "View"):
        print(f"Available Genres: {AvailableGenres}")
        print("What sort of genre do you want?")
        category = input("")
    if(category == "Pinball"):
        print(Arcade["Pinball"])
    elif(category == "Rhythm"):
        print(Arcade["Rhythm"])
    elif(category == "Racing"):
        print(Arcade["Racing"])
    elif(category == "Shooter"):
        print(Arcade["Shooter"])
    else:
        print("Invalid Input, do you want to enter status-mode?")
        statusinquiry = ""
        if(statusinquiry == "Yes"):
            print(Arcade["Pinball Wizard"]["Status"])
            print(Arcade["Alien Blaster"]["Status"])
            print(Arcade["Dance Floor X"]["Status"])
            print(Arcade["Retro Racer"]["Status"])
        elif(statusinquiry == "No"):
            print("Returning to normal..")
def AddingMachines():
    print("Which machine are you trying to add?")
    r = input("")
    print("And the key?")
    t = input("")
    Arcade[r] = f"{t}"
def RemovingMachines(): #I think it works, not even sure, however I'll probably work on it later, I'm sorry kye.
    print("Are you trying to remove the last item, or are you trying to remove a machine?")
    r = input("")
    if(r == "Last"):
        Arcade.popitem()
        print("Successfully Removed!")
    if(r == "Pinball"):
        Arcade.pop(Arcade['Pinball'])
    elif(r == "Rhythm"):
        Arcade.pop(Arcade['Rhythm'])
    elif(r == "Racing"):
        Arcade.pop(Arcade['Racing'])
    elif(r == "Shooter"):
        Arcade.pop(Arcade['Shooter'])
def UpdatingMachines(): #Not Working, not sure how to get it working either way.
    print("Which machine are you trying to update the status of?")
    r = input("")
    print("And the key?")
    t = input("")
    Arcade({f"{r}":f"{t}"})
    print("Successfully Updated!")
thing = True
r = "" 
t = ""
while(thing == True):
    print("Hello there, what do you need?\n")
    print(f"Available Functions: {Available}\n")
    t = input("")
    if(t == "View"):
        ViewingMachines()
    elif(t == "Add"):
        AddingMachines()
    elif(t == "Remove"):
        RemovingMachines()
    elif(t == "Update"):
        UpdatingMachines()
    else:
        print("Quitting..")
        exit(0)
    