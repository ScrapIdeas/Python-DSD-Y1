
import time
import os

games = [
    "Metal Gear Rising: Revengeance", "Devil May Cry 2"
]
availablefunctions = ["printoutgames", "favourite","played","playing"]
favourite = ""
played = ""
playing = ""
x = games
r = ""
loop = True

def printoutgames():
    number1 = 0
    print("Would you want me to display any popular games, or your favourites / Played?")
    r = input("")
    if(r == "Yes"):
        for x in games:
            number1 += 1
            print(f"[{number1}] {x}")
            time.sleep(1)
        time.sleep(5)
        os.system("CLS")
    elif(r == "Favourite"):
        print(f"Your Favourite Game: {favourite}")
        time.sleep(5)
        os.system("CLS")
    elif(r == "Played"):
        print(f"Your played games: {played}")
        time.sleep(5)
        os.system("CLS")

    else:
        print("Invalid input.")

def favouritegames():
    global favourite
    print("Which game would you want to favourite?")
    print(games)
    r = int(input())
    if(-1 < r > 4):
        print("Too high")
    else:
        favourite = games.pop(r)
        print("Game successfully favourited!")
def played():
    global played
    print("Which game would you want to mark as played?")
    print(games)
    r = int(input())
    if(-1 < r > 4):
        print("Too high")
    else:
        played = games.pop(r)
        print("Game Successfully Marked as Played!")
        

while(loop == True):
    print("Welcome to the Popular Game Tracker!")
    print("Which function would you prefer?")
    print(availablefunctions)
    r = input()
    if(r == "printout"):
        printoutgames()
        os.system("CLS")
    elif(r == "favourite"):
        favouritegames()
        os.system("CLS")
    elif(r == "playing"):
        playing()
        os.system("CLS")
    elif(r == "played"):
        played()
        os.system("CLS")


    
        



