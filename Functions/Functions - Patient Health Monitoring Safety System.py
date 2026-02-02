#Small Hospital Project.

import time
import os
cholesterol = int(0)
glucose = int(0)
units = str("")
patients = []
MULTIPLYBYORDIVIDE = int(18)
FEVERTHRESHOLD = int(38)
totalamountofpatients = int(0)
functionschoosing = True
loginoption = True
systemactive = True
functionsavailable2 = {"Unit Converter", "Temperature Checker","Patient Hydration Tracker","Heart Beat Tracker.","Register Now","View total amount of patients"}
staffID = int(3595)
staffaccess = False
stafffunctions = {"Reset Total Amount of Patients."}
#Did some bug fixes, so it should work just fine.

#New code here, did this here cause I wasn't in here last lesson and I don't really know what hospital system you're talking about, unless its this.
#This works.
def totalpatients():
     registeringperiod = True
     while(registeringperiod == True):
          global totalamountofpatients
          patients1 = input("Tell me your name.")
          patients.append(patients1)
          totalamountofpatients += 1
          r1 = input("Do you want to register anyone else?")
          r1.capitalize()
          if(r1.upper == "Yes"):
               registeringperiod = True
          else:
               break
     return patients
#This works.     
def viewtotal():
     print("Would you like to look at the total amount of patients currently registered?")
     r1 = input("")
     r1.capitalize() #Capitalizes, self-explanatory.
     if(r1 == "Yes"):
          print(patients) #Shows you the list.
          print(f"Total amount of patients registered: {totalamountofpatients}") #Prints number of patients available.

def resettotal():
     totalamountofpatients = totalamountofpatients - totalamountofpatients #Resets the amount of patients currently registered, doing it like this cause earlier it turned out odd and was kind of a headache, to be fair.
     print(f"Patient Log Successfully Cleared. Available Patients: {totalamountofpatients}")
     patients.clear() #Clears the list.
     print(f"Currently Registered Patients: {patients}")
     return totalamountofpatients
     



def UnitConverter():
    testisrunning2 = True
    testisrunning3 = True
    response1 = input("Greetings, What test would you like?\n") #Prompts the user as to what test they'd like.
    response1.capitalize()
    print("Glucose / Cholesterol")
    if(response1 == "Glucose"): # If its glucose, it starts glucose conversion.
     print("Starting Glucose..")
     glucose = input("Tell me the value for Glucose.")
     units = input("Tell me the Units.")
     print(f'Information Entered: {glucose} + {units}')
     time.sleep(5)
     print('Preparing Test..')
     time.sleep(5)
     while(testisrunning2 == True): #Loops due to the fact that I want to ask the user whether they want to do it again, if they don't, its set to false.
          response5 = input("Which way do you want me to convert, to mmol/L or mg/dL?\n")
          if(response5 == "mmol/L"):
                newtotal = int(glucose) * MULTIPLYBYORDIVIDE
                time.sleep(5)
                print(f"Unit Converted, {newtotal} mmol/L")
          elif(response5 == "mg/dL"):
                newtotal = int(glucose) / MULTIPLYBYORDIVIDE
                time.sleep(5)
                print(f"Unit Successfully Converted, {newtotal} mg/dL")
          elif(response5 != "mg/dL" or "mmol/L"):
               print("Unknown Unit, please try again.") #Some validation.
          response6 = input("Do you want to convert it yet again?") #The question.
          response6.capitalize()
          if(response6 == "Yes"):
               testisrunning2 == True #Starts over from response5.
               print("Starting Test Selection again..")
          elif(response6 == "No."):
               break

          elif(response1 == "Cholesterol"): #Same thing, but with Cholesterol.
               print("Starting Cholesterol..")
               cholesterol = input("Tell me the value for Cholesterol")
               units = input("Tell me the units.")
               print(f"Information Entered : {cholesterol} + {units}")
               time.sleep(5)
               print('Preparing test..')
               time.sleep(5)
               while(testisrunning3 == True):
                    response6 = input("Which way do you want me to convert, to mmol/L or mg/dL?\n")
                    if(response6 == "mmol/L"):
                         newamount = int(cholesterol) * MULTIPLYBYORDIVIDE
                         time.sleep(5)
                         print(f'Unit converted, {newamount} mmol/L')
                    elif(response6 == "mg/dL"):
                         newamount = int(cholesterol) * MULTIPLYBYORDIVIDE
                         time.sleep(5)
                         print(f'Unit converted, {newamount} mg/dL')
                    elif(response6 != "mg/dL" or "mmol/L"):
                         print("Unknown Unit, please enter it again.") #Some validation to ensure that they're entering what they're entering.
                    response8 = input("Do you want me to do it again?")
                    response8.capitalize()
                    if(response8 == "Yes"):
                         testisrunning3 == True
                    elif(response8 == "No"):
                         break
                   
          elif(response1 == "Quit"):
               print("Thank you for using the Cholesterol / Glucose Converter! \n")
               break
#Untested, unsure if it works properly but it should.
def TemperatureChecker():
     temperaturereadings = []
     amountoftimesentered = int(0)
     theaverage = float(0)
     enteringtemperature = True
     print("-------------------------------------------")
     print("Welcome to the Temperature Checker 9000!")
     print("Please provide me with 3 Temperature Readings from your current day!")
     print("-------------------------------------------")
     while(enteringtemperature == True and amountoftimesentered < 3): #Two conditions, checks if the boolean is true and if amountoftimesentered has crossed 3.
          #asks for the temperature.
          inputtemp = input("Please enter your temperature.")
          temperaturereadings.append(inputtemp)
          theaverage = theaverage + int(inputtemp) #Adds it to the average whilst also adding it to the list.
          amountoftimesentered = amountoftimesentered + 1 #Counts up by 1.
          if(amountoftimesentered == 3): #Once it has crossed 3, it'll start displaying the info whilst also breaking the loop.
               theaverage = theaverage / 3
               print(f"Temperature Entered: {temperaturereadings}") 
               print(f"The Average Temperature: {theaverage:.2f}")
               if(theaverage > FEVERTHRESHOLD): #If the user has crossed the  38 celsius threshold, it displays this.
                    print(f"Warning, the user is reaching the approximate Fever Threshold, Current Temperature: {theaverage:.2f} ")
               break
          
#Unsure if it works, untested.
def heartratechecker():
     age = int(0)
     restingheartrate = int(0)
     MAXIMUMHEARTRATEBASE = 220
     SAFEHEARTRATE = 100 #Same thing just like with enteredmaximumheartrate.
     enteredmaximumheartrate = False #Wanted to use this for a loop but I just left it here, for some reason.
     print("----------------------------------")
     print("Welcome to the Heart-Checker 9000!")
     print("Real Creative, I know.")
     print("Allow me to ask you for some things.")
     print("----------------------------------")
     restingheartrate = input("What is your heart rate when resting?") #Asks for the resting heart rate.
     print("..And")
     time.sleep(2)
     age = input("What is your age?") #Asks for age.
     print("Thank you for telling me these, time for calculations.")
     time.sleep(5)
     safemaximumheartrate = MAXIMUMHEARTRATEBASE - age #Does a calculation for safe maximum heart rate whilst the user waits.
     print("Calculating safe maximum heart rate..")
     time.sleep(5) #Classifies heartrate.
     print("Will display results after classifying your resting heart rate.")
     if(restingheartrate < 50):
          print("You are an athelete, your resting heart rate is around 50 BP/M!")
     elif(restingheartrate == 60 or 68):
          print(f"You are either very good, or above average, depending on what you put in as your BP/M is: {restingheartrate}")
     elif(restingheartrate == 69 or 76):
          print(f"You are either average, or below average. That is rather awful fella.  BP/M: {restingheartrate}")
     elif(restingheartrate >= 84):
          print(f"You're looking awful there, please maintain your heart. BP/M: {restingheartrate}")
          print(f"Plus, you're approaching the Safe HeartRate Threshold. SAFE BP/M: {SAFEHEARTRATE}")
     time.sleep(5) #Displays the maximumheartrate.
     print(f"Safe Maximum Heart Rate: {safemaximumheartrate}")

#Dunno if it works, didn't test.
def patienthydration():
     hydrationintake = float(0)
     DAILYGOAL = int(2 or 2.5)
     print("----------------------------------")
     print("Welcome to the last function.")
     print("The water-intake-asker!") #Don't ask about this odd name, just ran out of ideas.
     print("----------------------------------")
     
     print("----------------------------------")
     hydrationintake = input("What is your water intake?") #Asks for water intake.
     print(f"That is a rather.. interesting intake.  (Water Intake: {hydrationintake}L)") #Judges you for that water intake.
     if(hydrationintake < DAILYGOAL): #Does a calculation and compares it, then prints a message if they've met the goal or not.
          print("You're almost there in regards to your daily goal, keep going!")
          almostthere = DAILYGOAL - hydrationintake #Subtracts the intake frm the dailygoal to see how much they need.
          print(f"You're almost there, you were off by {almostthere}L!")
     elif(hydrationintake == DAILYGOAL):
          print("You're basically there, congratulations!")
          print(f"Hydration Goal Met, User's Hydration: {hydrationintake}L") #Displays a congratulations message.
     elif(hydrationintake >= DAILYGOAL):
          print("You're overdoing it.")
#Did a menu for the Functions, considering just leaving them here felt kind of lonely, and besides this is a good usage of my time I suppose.
while(loginoption == True):
     r3 = input("What is your preferred login option?  (Staff / Civilian)")
     if(r3 == "Staff"):
          r4 = int(input("Please enter the Staff Pin."))
          if(r4 != staffID):
               print("Access Denied.")
          elif(r4 == staffID):
               print(stafffunctions)
               staffaccess = True
               break
     elif(r3 == "Civillian"):
          print("Proceeding to normal functions..")
          break
     else:
          print("Please try again.")
while(systemactive == True):
     os.system('cls')
     print("Welcome to the Patient Health Monitoring System. :O)")
     print("Which Function would you like to use?  (Type in Quit to Quit.)")
     if(staffaccess == True):
               print(stafffunctions)
     print(functionsavailable2)
     while(functionschoosing == True):
          functionsavailable = input("")
          functionsavailable.capitalize()
          if(functionsavailable == "Unit Converter"):
               UnitConverter()
          elif(functionsavailable == "Temperature Checker"):
               TemperatureChecker()
          elif(functionsavailable == "Patient Hydration Tracker"):
               patienthydration()
          elif(functionsavailable == "Heart Beat Tracker"):
               heartratechecker()
          elif(functionsavailable == "View Total"):
               viewtotal()
          elif(functionsavailable == "Register Now"):
               totalpatients()
          elif(functionsavailable == "Reset Total" and staffaccess == True):
               resettotal()
          elif(functionsavailable != "Unit Converter" or "Temperature Checker" or "Patient Hydration Tracker" or "Heart Beat Tracker" or "View Total" or "Register Now"):
               print("That isn't one of the available functions, please try again.")
          elif(functionsavailable == "Quit"):
               print("Quitting.")
               time.sleep(5)
               exit(0)


     


            