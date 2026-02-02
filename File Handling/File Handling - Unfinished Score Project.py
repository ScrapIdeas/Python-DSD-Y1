score = 0
def asktheuser():
    print("What is your score?")
    score = int(input(""))
    with open("score.txt","a") as file:
        file.write(f"Your score: {score}")


def conversion():
    print("test1")


def highesttolowest():
    print("test1")