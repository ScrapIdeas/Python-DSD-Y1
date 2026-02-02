Attempts = 0
MaxAttempts = 3

RFIDAccessCard = 515
AccessPin = 2402738

informationvalidation = False
loginsystemonline = True

while(loginsystemonline == True):
    AP = int(input("Please put in your Access Pin."))
    RFID = int(input("Please scan your RFID Card."))
    loginsystemonline = False
    informationvalidation = True
while(informationvalidation == True):
    if(AP & RFID == AccessPin & RFIDAccessCard):
        print("Access Granted.")
        print("Door Mechanism Unlocked.")
        break
    if(AP & RFID != AccessPin & RFIDAccessCard):
        print("Invalid Information.")
        MaxAttempts = MaxAttempts - 1
        Attempts = Attempts + 1
        print(f"Attempts remaining: {MaxAttempts}")
        loginsystemonline = True
        informationvalidation = False
    elif(Attempts == 3):
        print("3 Attempts detected.")
        print("Calling Security Now..")
        print("Door Mechanism Locked.")
        break
    