import matplotlib.pyplot as plt
import time
import os

pickingafunction = True
calculating = False
calories = 0
workouttime = 0
steps = 0
timing = 0
amountoftablets = 0
amountofpeopledistributedto = 0
method = ("")
numberusedinthecaclculator = 0
LISTOFAVAILABLEFUNCTIONS = {" [1] CalorieBurn, [2] stepconversion, [3] medicationtiming, [4] heartrecovery, [5] medicinepackusage, [6] medicalcalculator."}
PARACETAMOLSAFEDOSAGE = 500
AVAILABLEMETHODS = {"+ - Addition.", "- - Subtract.", "/ - Divide.", "* - Multiply.", "// - Modulus"}
RECOVERYRATE = 120

#Works properly.
def CalorieBurn():
    print("Greetings, I'd like to see how many calories you've burnt.")
    time.sleep(5)
    calories = int(input("How many calories, exactly?\n"))
    workouttime = int(input("How many minutes or hours have you worked out?\n"))
    caloriesburnt = calories * workouttime
    time.sleep(5)
    print(f"This is how many calories you've burnt, approximately. : {caloriesburnt}")

#Works properly.
def stepconversion():
    print("Greetings, I'd like to see how many steps you've walked.")
    time.sleep(5)
    steps = int(input("How many steps exactly?\n"))
    newamountofsteps = steps / 1300
    time.sleep(5)
    print(f"Estimated Distance walked: {newamountofsteps}")

#Works properly.
def medicationtiming():
    print("I'll estimate when you need to take your medication.")
    timing = int(input("Give me the approximate minutes.\n"))
    hours = timing / 60
    minutes = timing // 60
    time.sleep(5)
    print(f"Approximate amount of hours: {hours}")
    time.sleep(5)
    print(f"Approximate amount of minutes: {minutes}")

#Works properly.
def medicinepackusage():
    print("I'll tell you the approximate amount of tablets leftover.")
    time.sleep(5)
    amountoftablets = int(input("What is the amount of tablets you're giving out?\n"))
    amountofpeopledistributedto = int(input("And the amount of people you're distributing it to?\n"))
    remainderoftablets = amountoftablets // amountofpeopledistributedto
    time.sleep(5)
    print(f"The remaining amount of tablets is: {remainderoftablets}")

def medicalcalculator():
    #Activates a loop which will allow the user to continously put in calculations.
    while(calculating == True):
        print("Greetings, Welcome to the Medical Calculator 9000.")
        method = str(input("Tell me, what type of method are you planning to use?"))
        print(AVAILABLEMETHODS)
        print("If you wanna quit, type in 'Quit'.")
        #Changes the method to: Addition
        if(method == "Addition"):
            print(" Time to calculate addition related things, such as how many patients are in this hospital!")
            numberyouregoingtouse = int(input("Tell me the amount of patients, for example. However anything can be used here."))
            numberusedinthecaclculator = numberusedinthecaclculator + numberyouregoingtouse
            print(f"The Result: {numberusedinthecaclculator} Patients.")
        #Changes the method to: Subtraction
        if(method == "Subtraction"):
           print( "This is just like addition, however this time we're going to see how many patients got released from the hospital this time.")
           numberyouregoingtouse = int(input("Tell me yet again, the number of patients that have gotten released from the hospital"))
           numberyouregoingtouse2 = int(input("Tell me the number of patients left in the hospital."))
           numberusedinthecaclculator = numberyouregoingtouse2 - numberyouregoingtouse
           print(f"Patients left in the hospital: {numberusedinthecaclculator}")
        #Changes the method to: Division
        if(method == "Division"):
           print("We're going to calculate dosage per kg.")
           response1 = input("What type of drug are you using? (Paracetammol's currently available.)\n")
           kg = int(input("How many KGs are you?\n"))
           totaldosage = response1 * kg
           print("And the amount of days you're going to take it for?")
           response1 = input()
           totaltotaldosage = totaldosage / response1
           print(f"The KG per dosage: {totaltotaldosage} ")
        #Changes the method to: Multiplication
        if(method == "Multiplication"):
           print("Do any calculation here, it doesn't necessarily matter if it will help you with your medical duties.")
           response1 = int(input("Number 1 here."))
           response2 = int(input("Number 2 here."))
           result = response1 * response2
           round(result)
           print(f"The result of that calculation was: {result}")
        #Changes the method to: Modulus
        if(method == "Modulus"):
           print("Yet again, do any calculation here.")
           response1 = int(input("Number 1 here."))
           response2 = int(input("Number 2 here."))
           result = response1 * response2
           round(result)
           print(f"The result of that calculation was: {result}")
        #Quits the loop by using a Break statement.
        if(method == "Quit"):
            print("Quitting the calculator..")
            break





#Works properly.
def heartrecovery():
    print("I'm here to model your recovery overtime.")
    time.sleep(5)
    initialstate = int(input("What is the current state your heart is in? \n"))
    #I don't know what you want me to do here.. so I'll just put this in here.
    Anotherrecoveryrate = 120 * (0.9 ** 5)
    time.sleep(5)
    plt.plot(initialstate, Anotherrecoveryrate) #Why is this so simple, yet I can't remember the fact that plt is for matplotlib?
    plt.show()
    plt.xlabel("Heart Recovery Rate.")
while(pickingafunction == True): #Loop for the menu, after you're doing choosing a function, it'll make you go back.
    print("Welcome to the Fitness Tracker App.")
    print("\033[1;40;40m", "Colour Set to: Purple.") #Searched up how to do this, turns out its very different from command prompt where you can just do colour B9 or something akong the lines of that.. :O(
    time.sleep(3)
    print(f"Please choose from the available functions. Available functions: {LISTOFAVAILABLEFUNCTIONS}")
    response1 = input()
    if(response1 == "CalorieBurn"):
        print("Turning on Calorie Burn..")
        time.sleep(5)
        CalorieBurn()
        time.sleep(10)
        os.system("cls")
    if(response1 == "stepconversion"):
        print("Turning on Step Conversion...")
        time.sleep(5)
        stepconversion()
        time.sleep(10)
        os.system("cls")
    if(response1 == "medicationtiming"):
        print("Turning on Medication Timing..")
        time.sleep(5)
        medicationtiming()
        time.sleep(10)
        os.system("cls")
    if(response1 == "medicinepackusage"):
        print("Turning on medication pack usage..")
        time.sleep(5)
        medicinepackusage()
        time.sleep(10)
        os.system("cls")
    elif(response1 == "heartrecovery"):
        print("Turning on Heart Recovery..")
        time.sleep(5)
        heartrecovery()
        time.sleep(10)
        os.system("cls")
    elif(response1 == "medicalcalculator"):
        print("Turning on the Medical Helper.")
        time.sleep(5)
        calculating = True
        medicalcalculator()
        time.sleep(10)
        os.system("cls")
    elif(response1 == "Quit"):
        print("Quitting the program shortly..")
        print("Or in 10 seconds, for that matter.")
        time.sleep(10)
        exit(0)
    try:(response1)
    except:
        print("You most likely didn't enter a valid function or something along those lines.")






