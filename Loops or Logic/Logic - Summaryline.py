def summaryline():
    score = 0
    water = 0
    steps = 0
    screen = 0
    percentsteps = 0
    GOAL = 10000
    SCREENMINS = 240

    steps = int(input("What are your steps?\n"))
    percentsteps = float(steps // GOAL * 100)
    water = int(input("What is the water intake?\n"))
    if(water == 250):
        score+=1
    elif(water >= 2000):
        score+=5
    screen = int(input("Screen time?\n"))
    if(screen > SCREENMINS):
        alert = ("HIGH")
    else:
        alert = ("OK")
    print(f"Steps: {steps}({percentsteps}%), Water: {water}ml (+{score} pts), Screen: {screen} --- {alert}")

summaryline()