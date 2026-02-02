import pandas as pd
import matplotlib.pyplot as plt
import time
import os
legosets = pd.read_csv("lego_sets.csv")#
AVAILABLE =[ "list_price","listpricevspiececount","top10legosets","Maxamount","Meanamount","Dataframe","Top5mostexpensivesets","ReviewsVsRating"]

def list_price():
    plt.title('List Pricing')
    plt.xlabel('Legos')
    plt.ylabel('List Pricing')

    plt.hist(legosets.head(35)['list_price'], bins=140)

    plt.show()

    time.sleep(25)
    os.system("CLS")

def listpricevspiececount():
    plt.title('List Pricing Vs Piece Count')
    plt.xlabel('List_Pricing')
    plt.ylabel('Piece Count')

    plt.scatter(legosets['piece_count'],legosets['list_price'])

    plt.show()
    time.sleep(25)
    os.system("CLS")

def top10legosets():
    plt.title("Top 10 Lego Sets")
    plt.xlabel("Rating")
    plt.ylabel("Lego Set")

    plt.barh(legosets.head(10)['set_name'],legosets.head(10)['star_rating'] )

    plt.show()

    time.sleep(25)
    os.system("CLS")

def Maxamount():
    print(legosets['list_price'].max())

    time.sleep(25)
    os.system("CLS")

def Meanamount():
    print(legosets['list_price'].mean())

    time.sleep(25)
    os.system("CLS")

def Dataframe():
    print("Preview: ")

    legosets.head(10)
    time.sleep(25)

    print("Dataframe: ")

    pd.DataFrame(legosets)
    legosets.dropna(inplace = True)
    print(legosets)
    time.sleep(25)
    os.system("CLS")

def Top5mostexpensivesets():
    print("This doesn't work yet.")
    True
    #plt.bar(legosets["list_price","set_name"].max())
    #plt.show()
def ReviewsVsRating():
    print("This doesn't work yet.")
    True

#pd.DataFrame.info(legosets)


print("Which function would you prefer?")
print(AVAILABLE)
while(True):
    r = input("")
    time.sleep(5)
    os.system("CLS")
    if(r == "list_price"):
        list_price()
        True
    if(r == "listpricevspiececount"):
        listpricevspiececount()
        True
    if(r == "top10legosets"):
        top10legosets()
        True
    if(r == "Maxamount"):
        Maxamount()
        True
    if(r == "Meanamount"):
        Meanamount()
        True
    if(r == "Dataframe"):
        Dataframe()
        True
    if(r == "Top5mostexpensivesets"):
        Top5mostexpensivesets()
        True
    if(r == "ReviewsVsRating"):
        ReviewsVsRating()
        True
    if(r != "list_price","listpricevspiececount","top10legosets","Maxamount","Meanamount","Dataframe","ReviewsVsRating"):
        print("Wrong, try again.")
        time.sleep(5)
        print(AVAILABLE)
        True
    elif(r == "Quit"):
        print("Quitting.")
        time.sleep(25)
        False
        exit(0)