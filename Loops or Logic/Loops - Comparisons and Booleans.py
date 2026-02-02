choices = ""
ChoosingChoice = True
while(ChoosingChoice == True):
    choices = str(input("Which result do you want to see?"))
    print("Results available: one, two, three, or four.")
    if(choices == "one"):
        5>3 and 2<4
        if(5>3 & 2<4):
            print("True, 5 is bigger than 3, whilst 2 is less than 4.")
    if(choices == "two"):
        6<2 or 10 == 10
        if(6<2 == True or 10 == 10):
            print("6 is less than 2.")
            print("Or if you've chosen the other condition, then 10 IS equal to 10.")
    if(choices == "three"):
        not(8 > 8)
        if(8 > 8):
            print("False. 8 is not bigger than 8.")
    if(choices == "four"):
        (7 < 5) or (9 == 9)
        print("This is true, 7 is is bigger (less than) 5, and 9 is equal to 9.")
    if(choices == "Quit"):
        exit(0)