import os #Used to clear the screen.
import time #Used to make it seem like the messages wait.
totalscore = []
totaltotalscore = 0
quiz = { #Dictionary containing the question, categeory and answer.
    "Questions" : {
        "Question1": {
            "Question" : "What year was the first Iphone released",
            "Category" : "General Knowledge",
            "Answer" : 2007,
            },
        "Question2": {
            "Question" : "Which company created the playstation?",
            "Category" : "General Knowledge",
            "Answer" : "Sony",
            },
        "Question3":{
            "Question" : "What is the most streamed song on Spotify?",
            "Category" : "Social Media",
            "Answer" : "Blinding Lights",
            },
        "Question4":{
            "Question" : "What is one of the games that I'm thinking about that came out around 3 years ago from Red Dead Redemption 2's Year of release?",
            "Category" : "Gaming",
            "Answer" : "The Witcher 3: Wild Hunt",
            },
        "Question5":{
            "Question" : "What is a Roguelike game that involves a Child and a Basement?",
            "Category" : "Gaming",
            "Answer" : "The Binding Of Isaac",
            },
        "Question6":{
            "Question" : "Which company tends to send out the most copyright strikes towards fangames related to their IP?",
            "Category" : "Gaming",
            "Answer" : "Nintendo",
            }
    }
}
def mocking(): #Version that mocks the player for not getting the full score, a fun way of taking my rage out on last lesson.
    time.sleep(2)
    print("How funny, your score hasn't even reached 5 yet.")
    time.sleep(2)
    print("But I suppose some of the questions could've been a tad bit difficult, though.. who cares?")
    time.sleep(2)
    print("Anyway..")
    time.sleep(4)
    print("Do you wish to continue, or do you want to restart?")
    print("Enter your answer below: ")
    r = input("")
    if(r == "Yes"):
        print(f"Your score: {score}")
        time.sleep(2)
        score = 0
        gamestart = True
        time.sleep(4)
        os.system("CLS")
    elif(r == "No"):
        print(f"Quitting..")
        time.sleep(2)
        exit(0)
    else:
        print("Not restarting huh?")
        time.sleep(2)
        print("Bold choice.")
        time.sleep(2)
        print("Starting the game again, then.")
        print("However, you're keeping your score.")
        time.sleep(5)
        os.system("CLS")
        gamestart = True
def scoreis5(score): #Version of the end incase you got to 5.
    print("Oh, you've got around the score I'd expect you to have.")
    time.sleep(2)
    print("Time to make your choice, do you want to go into Infinite mode, or do you want to quit?")
    print("Your choice below: ")
    r = input("")
    if(r == "Infinite"):
        print("Not restarting huh?")
        time.sleep(2)
        print("Bold choice.")
        time.sleep(2)
        print("Starting the game again, then.")
        print("However, you're keeping your score.")
        time.sleep(5)
        os.system("CLS")
        gamestart = True
    else:
        print("Quitting it is then!")
        time.sleep(5)
        print(f"Your score: {score}")
        time.sleep(5)
        exit(0)
    


score = 0 #Use for the scoring system.
gamestart = True # Used for the loop.
while(gamestart == True): # Enjoy the cluster#### of code below, I am NOT about to use randomness to pick each question, no way in hell.
    if(5 == score < 6):
        print("Starting Infinite Mode.")
        time.sleep(2)
        print("See how big of a score you can get!")
        time.sleep(2)
        print("Unfortunately.. the developer is too lazy to implement new questions so you're stuck with the same ones.")
        time.sleep(2)
        print("Try to break the program or something, god knows.")
        time.sleep(4)
        os.system("CLS")
    print("Question: ")
    print(quiz["Questions"]['Question1']['Question'])
    print("Category: ")
    print(quiz["Questions"]['Question1']['Category'])
    print("Enter your answer below (Numbers, please.): ")
    r = int(input(""))
    if(r == 2007):
        time.sleep(1)
        print("Correct answer!")
        time.sleep(3)
        score+=1
        print(f"Score: {score}")
        time.sleep(3)
        os.system("CLS")
    else:
        print("Incorrect Answer!")
        time.sleep(3)
        os.system("CLS")
    print("Question: ")
    print(quiz["Questions"]['Question2']['Question'])
    print("Category: ")
    print(quiz["Questions"]['Question2']['Category'])
    print("Enter your answer below: ")
    r = input("")
    if(r == "Sony"):
        time.sleep(1)
        print("Correct answer!")
        time.sleep(3)
        score+=1
        print(f"Score: {score}")
        time.sleep(3)
        os.system("CLS")
    else:
        print("Incorrect Answer!")
        print("Correct Answer: Sony")
        time.sleep(3)
        os.system("CLS")
    print("Question: ")
    print(quiz['Questions']['Question3']['Question'])
    print("Category: ")
    print(quiz["Questions"]['Question3']['Category'])
    print("Enter your answer below: ")
    r = input("")
    if(r == "Blinding Lights"):
        time.sleep(1)
        print("Correct answer!")
        time.sleep(3)
        score+=1
        print(f"Score: {score}")
        time.sleep(3)
        os.system("CLS")
    else:
        print("Incorrect Answer!")
        print("Correct Answer: Blinding Lights")
        time.sleep(3)
        os.system("CLS")
    print("Question: ")
    print(quiz["Questions"]['Question4']['Question'])
    print("Category: ")
    print(quiz["Questions"]['Question4']['Category'])
    print("Enter your answer below: ")
    r = input("")
    if(r == "The Witcher 3: Wild Hunt"):
        time.sleep(1)
        print("Correct answer!")
        time.sleep(3)
        score+=1
        print(f"Score: {score}")
        time.sleep(3)
        os.system("CLS")
    else:
        print("Incorrect Answer!")
        print("The answer was: The Witcher 3: Wild Hunt ")
        time.sleep(3)
        os.system("CLS")
    print("Question: ")
    print(quiz["Questions"]['Question5']['Question'])
    print(f"Category: ")
    print(quiz["Questions"]['Question5']['Category'])
    print("Enter your answer below: ")
    r = input("")
    if(r == "The Binding Of Isaac" | "The Binding Of Isaac Rebirth" | "The Binding Of Isaac Afterbirth" | "The Binding Of Isaac Afterbirth+" | "The Binding Of Isaac Repentance" ):
        time.sleep(1)
        print("Correct answer!")
        time.sleep(3)
        score+=1
        print(f"Score: {score}")
        time.sleep(3)
        os.system("CLS")
    else:
        print("Incorrect Answer!")
        print("The Answers were: The Binding Of Isaac,")
        print("DLC: The Binding Of Isaac Rebirth,")
        print("DLC: The Binding Of Isaac Afterbirth,")
        print("DLC: The Binding Of Isaac Afterbirth+,")
        print("DLC: The Binding Of Isaac Repentance")
        time.sleep(3)
        os.system("CLS")
    time.sleep(2)
    print("Keep in mind there was probably another question that I had ready, but I forgot to implement it in advance. :O(")
    print("To be fair, I was just too glad to have this awful #### actually work.")
    time.sleep(6)
    os.system("CLS")
    if(score == 5):
        scoreis5(score)
        totalscore.append(score)
    elif(score < 5):
        mocking()
        totalscore.append(score)
    else:
        gamestart = True
