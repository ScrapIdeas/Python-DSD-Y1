import os
import time
Movies = ["Beetlejuice","GhostBusters","Hocus Pocus", "The Nightmare Before Christmas", "Casper"]
availablefunctions = {"view - View all currently available movies.","add - Add a new movie.", "remove - Remove a movie.","find - Find a Movie.","Quit - Quit the program."}
screens = {
    "Beetlejuice" : "Screen 1",
    "Ghostbusters" : "Screen 2",
    "Hocus Pocus": "Screen 3",
    "The Nightmare Before Christmas" : "Screen 4",
    "Casper" : "Screen 5"
}
r = ""
online = True

def remove():
    r = input("What movie would you like to remove?\n")
    Movies.remove(r)
    os.system("CLS")
    print("Movie Removed!")
    print(Movies)
    time.sleep(2)
    os.system("CLS")
def add():
    r = input("What movie would you like to add?\n")
    Movies.append(r)
    os.system("CLS")
    print("Movie Added!")
    print(Movies)
    time.sleep(2)
    os.system("CLS")
def view():
    print(f"Available Movies: {Movies}")
def find():
    print("Which movie are you trying to find?")
    print(Movies)
    r = input("")
    if(r == Movies[0]):
        print(screens["Beetlejuice"])
        time.sleep(3)
        os.system("CLS")
    if(r == Movies[1]):
        print(screens['Ghostbusters'])
        time.sleep(3)
        os.system("CLS")
    if(r == Movies[2]):
        print(screens["Hocus Pocus"])
        time.sleep(3)
        os.system("CLS")
    if(r == Movies[3]):
        print(screens["The Nightmare Before Christmas"])
        time.sleep(3)
        os.system("CLS")
    elif(r == Movies[4]):
        print(screens["Casper"])
        time.sleep(3)
        os.system("CLS")

while(online == True):
    print("Welcome to the Cinema Booking System!")
    print("Which movie would you like to book for?")
    print("And which function would you like to use?")
    print(availablefunctions)
    r = input("")
    if(r == "view"):
        view()
        time.sleep(3)
        os.system("CLS")
    if(r == "find"):
        find()
        os.system("CLS")
    if(r == "add"):
        add()
        os.system("CLS")
    if(r == "remove"):
        remove()
        os.system("CLS")
    elif(r == "Quit"):
        exit(0)