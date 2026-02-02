thisisathingyouask = ("")
nameIstore = ("")
l = True
while l == True:
    thisisathingyouask = input("Type in a name.")
    nameIstore = len(thisisathingyouask)
    if(nameIstore >= 20):
        print("Error: Sentence has more than or equal to 20 characters, try again.\n")
    else:
        print(thisisathingyouask + ", Hello there!\n")
        break