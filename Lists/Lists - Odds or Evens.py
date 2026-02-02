a = 10
b = 3
firsttestscore = a / b
secondtestscore = a // b
thirdtestscore = a*2.5
testlinkscores = [firsttestscore, secondtestscore, thirdtestscore,]
response = input("Would you like to put in more scores?\n")
addingtestscores = True
while addingtestscores == True:
    if(response == "Yes"):
      thingyouwantedtoadd = 0
      thingyouwantedtoadd = input("Enter a test score.")
      testlinkscores.append(thingyouwantedtoadd)
    response2 = input("Would you like to quit?")
    if(response2 == "Yes"):
        break
    else:
        addingtestscores = True
print("here are your scores. \n")
print(testlinkscores)
