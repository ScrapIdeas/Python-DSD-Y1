loop = True
user1 = False
user2 = False
choosingday = False
notifications = [34,28,55,40,60,22,18]
def totalnotifications():
    for x in notifications:
        print(notifications[x])
def biggestandsmallest():
    print("Calculating which day is the highest and lowest..")
    biggestnumber = max(notifications)
    smallestnumber = min(notifications)
    print(f"Smallest day: {smallestnumber}")
    print(f"Biggest day: {biggestnumber}")
def comparing():
    print("Numbers to compare.")
    print(notifications)
    print("Number 1:")
    r = input()
    print("Number 2:")
    b = input()
    if(r > b):
            comparison = f"{r} is bigger than {b}"
    if(r < b):
            comparison = f"{r} is smaller than {b}"
    elif(r == b):
            comparison = f"{r} is equal to {b}"
    print(comparison)
def choseday():
        r = input("Which day is it?  [1 - 7]")
        match r:
            case 0:
                print(f"The corresponding notification to day: {notifications[0]}")
            case 1:
                print(f"The corresponding notification to day: {notifications[1]}")
            case 2:
                print(F"The corresponding notification to day: {notifications[2]}")
            case 3:
                print(F"The corresponding notification to day: {notifications[3]}")
            case 4:
                print(F"The corresponding notification to day: {notifications[4]}")
            case 5:
                print(F"The corresponding notification to day: {notifications[5]}")
            case 5:
                print(F"The corresponding notification to day: {notifications[6]}")
            case default:
                r = input("Are you done choosing?")
                if(r == "Yes"):
                    choosingday == False
                elif(r == "No"):
                    choosingday == True
def appending():
     r = input("What do you want to add?")
     notifications.append(r)
     print(notifications)
     print("updated.")
def highestnumber():
     big = max(notifications)
     small = min(notifications)
     print(small)
     print(big)
     





while(loop):
    print("Hello, welcome to the Notifications Software!")
    r = input("Which user is currently using this device?")
    if(r == "User 1"):
        print("User Accepted, User1 Logging on..")
        user1 = True
    if(r == "User 2"):
        print("User Accepted, User2 Logging on..")
        user2 = True
    else:
        print("Wrong User, please try again.")
        loop = True
    

    if(user1 | user2 == True):
        print("Welcome to the Notifications S0ftware!")
        print("Which function would you like to do? ")
        print("[1] - Corresponding Day, [2] - Comparisons (or Comparisons2), [3] - Total Notifications, [4], I dont have enough time to do the last task, sorry kye.\n")
        r = input()
        if(r == "Corresponding Day"):
             choseday()
        if(r == "Comparisons"):
             comparing()
        if(r == "Comparisons2"):
             biggestandsmallest()
        if(r == "Total Notifications"):
            totalnotifications()