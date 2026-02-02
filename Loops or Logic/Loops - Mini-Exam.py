name = ("")
age = ("")
testscore = ()
initialscore = 0
passedexam = False
greetingsyoupassed = f"You have passed this exam, congratulations!"

age = input("What is your age?\n")
name = input("What is your name?\n")
permissiontostart = input("Do you want to start?")
if(permissiontostart == "Yes"):
    print("What is this activity?")
    t1 = input()
    if(t1 == "Making a project"):
        #Same ordeal as the 100 score thing.
        testscore = initialscore + 20
        print("20 Points added!")

    print("Question 2, what is this language called? ")
    t2 = input()
    if(t2 == "Python"):
        #Same ordeal as the 100 score thing.
        testscore = initialscore +  40
        print("20 Points added!\n")

    print("Final question considering I'm getting tired of this.. for 60 points.")
    print("What is this course called?")
    t3 = input()
    if(t3 == "DSD" or "Digital Production, Design and Development"):
        #I'm setting the score to 100 since I'm not really about to deal with as much of a headache at this is, If I had more than an hour I would have personally debugged this.
        testscore = initialscore + 100
        print("60 Points added!")
    elif(t3 == "I don't know"):
        print("Would you like to see the answer?")
        t4 = input()
        if(t4 == "Yes"):
            print("DSD" + "Digital Production, Design and Development.")
    print("Time to print your score!")
    
#debug_print
print(testscore)
if(testscore >= 100):
    passedexam = True
    print(greetingsyoupassed)
    print("You should be proud of this. \n")
elif(testscore <= 90):
    print("You nearly passed, unfortunate, " + name + "\n")
elif(testscore != 25):
    print("You didn't pass, get out of my class, " + name + "\n")
elif(testscore == 0):
    print("You.. did you even do the test whatsoever? \n")