import os
import time
playlist = []
availablefunctions = {"Sort", "Add", "Remove", "Display"}
r = ""
HARDTHRESHOLD = 5
b = True
def Sort():
    playlist.sort()
    print("Playlist Sorted!")
    print(playlist)
    time.sleep(5)
    os.system("CLS")
def Add():
    n = 0
    if(n == HARDTHRESHOLD):
        print("Threshold limit reached, please remove some songs.")
    r = input("What song do you want to add to the playlist?\n")
    playlist.append(r)
    n = n + 1
    os.system("CLS")
    print("Added to playlist!")
    print(playlist)
    time.sleep(5)
    os.system("CLS")
def Remove():
    r = input("What do you want to remove frm the playlist?\n")
    playlist.remove(r)
    os.system("CLS")
    print("Removed from the playlist!")
    print(playlist)
    time.sleep(5)
    os.system("CLS")
def Display():
    print(playlist)
    time.sleep(5)
    os.system("CLS")

while(b == True):
    print("Welcome to the Playlist Manager!")
    print("Which one would you like to do?")
    print("Type in 'Quit' to quit.")
    print(availablefunctions)
    r2 = input("")
    time.sleep(1)
    os.system("CLS")
    if(r2 == "Add"):
        Add()
        os.system("CLS")
    if(r2 == "Sort"):
        Sort()
        os.system("CLS")
    if(r2 == "Remove"):
        os.system("CLS")
        Remove()
    if(r2 == "Display"):
        os.system("CLS")
        Display()
    elif(r2 == "Quit"):
        quit()