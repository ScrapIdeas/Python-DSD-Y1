bankbalancetransfer = float(35.00)
pin = int()
realpin = 3653
name = ("")
tryagain = True
takingoutcash = True
takingoutcash2 = True

name = input("What is your name?")
pin = input("What is your pin?")
if(pin == 3653):
 print("Access granted.")
 #Would've implemented a while loop here, but it's yet again too much of a headache.
 while(takingoutcash2 == True):
  print("What amount of cash would you like to take out? ")
  takingcash = float(input())
  print(f"Currently available cash: {bankbalancetransfer}")
while(takingoutcash == True):
 if(takingcash >= 35):
  print("Cannot take out that amount of cash unless you want to go completely bankrupt.")
  break
 else:
   newamount = bankbalancetransfer - takingcash
   print("This is your new amount, are you satisfied with this?")
   print(f"New amount of cash: {newamount}")
   break