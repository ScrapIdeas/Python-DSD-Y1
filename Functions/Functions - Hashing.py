passwords = []
usernames = []
active = True
active2 = False
captcha = False
loggedinbefore = False
def hashingpasswords():
    hash(pr)
    passwords.append(pr)
def hashingusernames():
    hash(ur)
    usernames.append(ur)

print("Welcome to the secure authentication system!")
while(active == True):
    pr = input("Enter your password: ")
    if(pr != isinstance(pr,str)):
        print("Incorrect format.")
        active = True

    if(pr != loggedinbefore == True & passwords[0]):
        print("Incorrect Password.")
        active = True
    else:
        hashingpasswords()
        active = False
        active2 = True
        
while(active2 == True):
    ur = input("Enter your username: ")
    if(ur != isinstance(ur,str)):
        print("Incorrect format.")
        active2 = True
    if(ur != loggedinbefore == True & usernames[0]):
        print("Incorrect Username.")
        active2 = True
    else:
        hashingusernames()

