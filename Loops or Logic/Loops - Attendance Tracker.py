initialtemp = 0
t = 0
loop = True
celsiustemp = float(0)
import time
while(loop == True):
 initialtemp = input("What temperature do you want?\n")
 if(initialtemp == "Kelvin"):
    celsiustemp = input("What temperature is it for you in celsius?")
    resulttemp = int(celsiustemp) + 273.15
    print(celsiustemp + "K" + " <--- This is your temperature in Kelvin.")
 elif(initialtemp == "Celsius"):
    question = input("What type of temperature are you going to put in?")
    if(question == "Fahrenheit"):
       t = input("What is the temperature?")
       resulttemp = (9/5 * t ) + 32
       print(resulttemp + "F" + "<-- Temperature.")
    if(question == "Celsius"):
        t = input("What is the temperature? (Kelvin edition.)")
        resulttemp = t - 273.15
        print(resulttemp + "C" + "<-- Temperature.")
    if(question == "Kelvin"):
        t = input("What is the temperature in Celsius?")
        resulttemp = t + 273.15
        print(resulttemp + "K" + "<-- Temperature.")
 else:
    loop = False
    print('Quitting..')
    time.sleep(5)
    print("Bye-bye!")
    time.sleep(2)
    exit(0)