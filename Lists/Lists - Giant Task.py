someonesheight = []
Theircash = []
YesOrNo = []
PhoneNumber = []
Address = []
#Made these just for the sole purpose of making everything easier for myself in the long run, even if it looks messy.
response = ("")
 #For the user to be capable of entering a number multiple times, I've used a while loop which can be closed when the user just types in ''Quit'', which will then use break to close the loop.
variableforaloop = True
while(variableforaloop == True):
    #Considering Python usually guesses data types, it doesn't necessarily matter what I enter, therefore not needing to assign a specific data type to response.
    response = input("Type in either a cash amount, Yes or no, a Phone Number, an address, or a person's height.\n")
    response2 = input("What would you like to put that in?\n")
    #Adds it to cash.
    if(response2 == "Cash"):
        Theircash.append(response)
    #adds it to yes or no.
    elif(response2 == "YesOrNo"):
        YesOrNo.append(response)
     #adds it to the phone number column, considering phone numbers usually are integers.
    elif(response2 == "PhoneNumber"):
        PhoneNumber.append(response)
     #Adds it to the address.
    elif(response2 == "Address"):
        Address.append(response)
     #Adds it to height.
    elif(response2 == "Height"):
        someonesheight.append(response)
     #Makes the user quit the program, and prints out the results.
    elif(response2 == "Quit"):
        response3 = input("Do you want to quit?")
        if(response3 == "Yes"):
            print(someonesheight, "<---", " Height.")
            print(Theircash, "<---", " Cash.")
            print(PhoneNumber, "<---", " Phone Numbers.")
            print(Address, "<---", " Addresses.")
            print(YesOrNo, "<---", " Yes Or No.")
            break

