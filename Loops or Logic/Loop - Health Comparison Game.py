#HealthComparisonGame
import time
import os

glucosetoday = 0
glucoseyesterday = 0
steptoday = 0
stepyesterday = 0
score = 0
loop = True
HEALTHYSTEPTHRESHOLD = 7000
HEALTHYGLUCOSETHRESHOLD = 140
GAMEESTARTED = False
OPTIONSMENU = False
DECISIONMAKING = False

def optionsmenu():
    while(OPTIONSMENU == True):
        print("Welcome to the OPTIONS Menu!")
        print("Here you can do a few things, but you can also go back to the actual menu.")
        print("What do you want to do?  [RESET SCORE], [SET SCORE], [To be added.] or 'QUIT'")
        response1 = input("")
    if(response1 == "Reset Score"):
        score = 0
        print(f"Score Successfully Reset! Current Score: {score}")
        time.sleep(2)
        os.system("CLS")
    elif(response1 == "Set Score"):
        print("Set score to what?")
        settingscore = input("")
        print(f"Settting Score to {settingscore}..")
        time.sleep(2)
        print(f"Score set! Score: {score}")
        time.sleep(2)
        os.system("CLS")
    elif(response1 == "quit" or "Quit"):
        OPTIONSMENU = False
        loop = True
        os.system("CLS")
def GAMESTARTED():
    while(GAMEESTARTED == True):
        glucosetoday = int(input("Please tell me the amount of glucose you've had today."))
        time.sleep(1)
        glucoseyesterday = int(input("Please tell me the amount of glucose you had yesterday."))
        time.sleep(1) 
    if(glucosetoday < glucoseyesterday):
        print("You've improved drastically, good job! Point Added!")
        score+=1
    steptoday = int(input("Now tell me the amount of steps"))
    time.sleep(1)
    stepyesterday = int(input("Steps yesterday?"))
    if(steptoday < stepyesterday):
        print("Once again, you've improved! Point added!")
        score+=1 
    time.sleep(1)
    print(f"Current Score = {score}")
    print("Do you want to keep going?")
    DECISIONMAKING = True
    while(DECISIONMAKING == True):
        decision = input("")
        if(decision == "Yes"):
            print("Alrighty!")
            time.sleep(2)
            DECISIONMAKING = False
            GAMEESTARTED = True
            os.system("CLS")
        if(decision == "No" | "no"):
            print("Alright then, Stopping the game.")
            time.sleep(2)
            DECISIONMAKING = False
            GAMEESTARTED = False
            loop = True
            os.system("CLS")
loop = True
while(loop == True):
    print("Welcome to the Health Comparison Game!")
    print("Which way do you want to go, Start, Options, or Quit?")
    response1 = input("")
    if(response1 == "Start"):
        GAMESTARTED()
        Loop = False
        os.system("CLS")
    elif(response1 == "Options"):
        Loop = False
        optionsmenu()
        os.system("CLS")
    elif(response1 == "Quit"):
        print("Quitting..")
        time.sleep(2)
        exit(0)
