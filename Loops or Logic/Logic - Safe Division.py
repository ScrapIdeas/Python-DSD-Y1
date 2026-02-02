totalminutes = 0
sessions = 0
def safe_average_minutes():
    totalminutes = int(input("Give me your total minutes."))
    sessions = int(input("Give me your total sessions."))
    if(sessions == 0):
        print("0")
    else:
        avg = totalminutes / sessions
        print(f"Average minutes per session: {round(avg,1)}")


safe_average_minutes()
