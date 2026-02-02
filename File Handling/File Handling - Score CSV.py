import csv
import os
import time
scores = [""]
notongithub = True
FILENAME = "scores.csv"
def add_score(username, score):
    if(score > 100):
        print("Too high.")
    if(score < 0):
        print("Too low.")
    else:
        with open("scores.csv","a",newline="") as file:
            writer = csv.writer(file)
            writer.writerow([f"Username:{username}"])
            writer.writerow([f"Score: {score}"])
            print("Score(s) successfully appended.")
            time.sleep(1)
            os.system("CLS")
    pass

def show_scores():
    os.system("CLS")
    for line in open("scores.csv"):
        csv_row = line.split()
        print(csv_row)   
        time.sleep(3)
    pass
def leaderboard():
    print("Somehow, I broke this function, lol.")
    time.sleep(1)
    print("For clarification, this worked perfectly fine before")
    scores.sort(reverse=True)
    print("Current Leaderboard: ")
    print(scores)
    time.sleep(1)
    os.system("CLS")



def main():
    if(notongithub == True):
        print("This is not on github, sorry not sorry lol.")
        notongithub = False
    while True:
        print("\n1. Add score")
        print("2. Show all scores")
        print("3. Quit")
        print("4. Leaderboard")
        choice = input("Choose an option: ")
        if choice == "1":
            username = input("Enter username: ")
            score = int(input("Enter score: "))
            scores.append(score)
            time.sleep(1)
            os.system("CLS")
            add_score(username, score)
        elif choice == "2":
            show_scores()
            time.sleep(1)
            os.system("CLS")
        elif choice == "3":
            print("Goodbye!")
            break
        elif choice == "4":
            leaderboard()
            time.sleep(1)
            os.system("CLS")
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()