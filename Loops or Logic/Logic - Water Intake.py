import time
import os
water_ml = 0
score = 0
gameloop = True

while(gameloop == True):
    water_ml = int(input("What is your total water intake?"))
    if(water_ml == 250):
        score+=1
        print(f"Score: {score}")
        time.sleep(5)
        os.system("CLS")
    elif(water_ml == 250*8):
        score+=5
        print(f"Score: {score}")
        time.sleep(5)
        os.system("CLS")
    elif(water_ml == 1):
        score = 15
    if(score >= 15):
        print("Do you want to quit?")
        r = input("")
        if(r == "Yes"):
            print(f"Total score = {score}")
            time.sleep(5)
            exit(0)
        else:
            gameloop = True