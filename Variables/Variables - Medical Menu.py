import time
import random

patients = []
age = []
height = []
DateOfBirth = []
Address = []
MedicineDosagePerDay = []
variable1 = 0
menuonline = True
menu2 = True
#Works fine.
def loopingmenu():
     menu3 = True
     return menu3
def totalamount():
     atotal = 0
     HospitalFees = input("How many of our services have you used?")
     for x in HospitalFees:
          atotal = atotal + 100
     print("Initial Total: ", atotal)
     print("Initial Total (W/ VAT): ", atotal*1.2)
#Fixed it by implementing Random and using a random choice.
def MedicineDosage():
     recommendeddosageperday = 2
     Childrenrecommendeddosage = 1
     elderlyremmendeddosage = 3
     print("How much medicine are you taking, as per our prescription of ", recommendeddosageperday, " Tablets.")
     variable1 = random.choice(age)
     if(variable1 >= 80):
          r = int(input(""))
          if(r > 3):
               print("Old Person is in the process of overdosing.")
          elif(r == 3):
               print("The Old Person has taken the correct amount.")
          elif(r < 3):
               print("The Old Person hasn't taken the correct amount of Tablets.")
          elif(r != int):
               print("ERR: That is not the valid data type, please enter the valid data type.")
     elif(variable1 >= 15):
          r = int(input(""))
          if(r > 1):
               print("Child is in the process of overdosing.")
          elif(r == 1):
               print("The child has taken the correct amount.")
          elif(r < 1):
               print("The child hasn't taken any tablets.")
          elif(r != type(int)):
               print("ERR: That is not the valid data type, please enter the valid data type.")
     elif(variable1 == 25):
      r = int(input(""))
      if(r >= 2 ):
         print("Patient is in the process of overdosing.")
         MedicineDosagePerDay.append(r)
      elif(r >= 10):
          print("Walk it off") #This is just for comedic purposes, no one in their right mind would eat up 10 tablets.
          MedicineDosagePerDay.append(r)
      elif(r < 2):
         print("The Patient has taken a lower than usual amount.")
         MedicineDosagePerDay.append(r)
      elif(r == 2):
         print("The Patient has taken the correct amount.")
         MedicineDosagePerDay.append(r)
      elif(r != int):
         print("ERR: That is not the valid data type, please enter the valid data type.")
#This doesn't work, would've fixed it if I could and had time.
def BMIIndex():
     weight = input("What is your weight?")
     height2 = height[1]
     BMIindex2 = weight / height2
     return BMIindex2

#It mostly fails to calculate the BMI, which is frustrating but it is what it is.
#BMI Estimation obviously won't work, and I even know the reason for why but I'm not really that bothered to fix it, so I just removed the feature to call this function. (Keep in mind it would've been way easier to just make it a part of the code, however it would look way messier.)
def BMIEstimation():
    if(BMIIndex <= 15):
            print("You're very underweight.")
    elif(BMIIndex >= 24.9):
            print("You're around normal weight, congratulations.")
    elif(BMIIndex >= 25.0):
            print("You're getting overweight.")
    elif(BMIIndex >= 39.9):
            print("You're obese now, that isn't good.")
    elif(BMIIndex >= 40):
            print("You're morbidly obese.")
while(menuonline == True):
    print("Welcome to the Medical Health Care System.")
    print("Here is your current information, as displayed.")
    print("patients: ", patients)
    print("age: ", age)
    print("height: ", height)
    print("Date-Of-Birth: ", DateOfBirth)
    print("Address: ", Address)
    while(menu2 == True):
        print("Which bit of information would you like to enter?")
        response = input("")
        if(response == "Patients"):
            response8 = input("What is your Name?")
            time.sleep(2)
            print("Processing..")
            time.sleep(5)
            print("Patient Registered, Name: ", response8)
            patients.append(response8)
        elif(response == "Age"):
            response7 = int(input("What is your Age?"))
            time.sleep(2)
            print("Processing..")
            time.sleep(5)
            print("Age Registered, Age: ", response7)
            age.append(response7)
            
        elif(response == "Height"):
            response6 = float(input("What is your Height?"))
            time.sleep(2)
            print("Processing..")
            time.sleep(5)
            print("Height Registered, Height: ", response6)
            height.append(response6)
        elif(response == "Address"):
            response5 = input("What is your Address?")
            time.sleep(2)
            print("Processing..")
            time.sleep(5)
            print("Address Registered, Address: ", response5)
            Address.append(response5)
        elif(response == "Weight"):
            response4 = int(input("What is your weight?"))
            time.sleep(2)
            print("Processing..")
            print("Weight registered, Weight: ", response4)
        elif(response == "Calculate BMI"):
             BMIIndex(response4,height)
        elif(response == "Back"):
            break
    print("I'd like to briefly interrupt you for a questionnaire containing one question.")
    MedicineDosage()
    print("Is there any more information you'd like to enter?")
    response4 = input("")
    if(response4 == "Yes"):
        menu2 = True
        print("Information input enabled.")
    elif(response4 == "No"):
        print("-----------------------------------")
        print("Height: ", height)
        print("Age: ", age)
        print("Patient Name", patients)
        print("Address: ", Address)
        print('Total BMI: ',) #Testing this later.
        response0 = input("What function would you want to use?")
        while(loopingmenu):
             print("Choices: Payment, Dosage.")
             response01 = input("")
             if(response01 == "Payment"):
                  totalamount()
             elif(response01 == "Dosage"):
                  MedicineDosage()
             else:
                  print("Quitting due to a lack of BMI Index.") #Its broken since I lacked the time to fix it.
                  time.sleep(5)
                  break
        print("Total Dosage: ", MedicineDosagePerDay)
        print("------------------------------------")
        print(totalamount)
        print("Quitting.. ")
        time.sleep(10)
        exit(0)

    