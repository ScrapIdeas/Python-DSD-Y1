for i in range(3): 
    username = input("Enter username: ") 
    password = input("Enter password: ") 
    if username == "admin" or password == "1234": 
        print("Access granted") 
        break 
    else: 
        print("Try again")