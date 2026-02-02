daily_screen_time_minutes = 0
DAILYTIME = 240
steps = 0
night_screen_minutes = 0
r = 0
def flag_user():
    if(daily_screen_time_minutes > 240 and steps < 5000):
        print("Uh-Oh, You've went past your daily amount of allowed time!")
        print(f"You're only allowed {DAILYTIME} Minutes of screen time!")
    elif(night_screen_minutes > 60):
        print("Uh-oh.")



daily_screen_time_minutes = int(input("What are your minutes of screentime currently?"))
steps = int(input("What is the amount of steps you've taken?"))
night_screen_minutes= int(input("And how many minutes have you spent at night on your screen?"))
flag_user()