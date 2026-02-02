loans = [
    {
        "loan_id" : 1,
        "student_name" : "",
        "student_id" : "",
        "device_type" : "",
        "device_id" : "",
        "date_out" : "",
        "due_back" : "",
        "returned" : False
    }
]
flag = True

def updateloan():
    inp = int(input("What Loan do you plan to update? [1 - 5]\n"))
    print([loans])
    match(inp):
        case 1:
            print("Which bit do you want to update?")
            print("Loan Number?\n")
            bittybit = int(input())
            bit = input(" Loan-Id, Student_Name, Student ID, Device Type, Device ID, Date out, Due_back or if its returned?")
            print(f"Chosen: {bit}")
            bit2 = input("What do you want to update it to?")
            chosenbit = bit
            loans[bit] #Unfinished

def viewallloans():
    print("Which Loan would you like to view? [1 - 5]")
    t = int(input(""))
    match(t):
        case 1:
            print(loans[0])
        case 2:
            print(loans[1])
        case 3:
            print(loans[2])
        case 4:
            print(loans[3])
        case 5:
            print(loans[4])
#I. have no idea why this function doesn't get called, but it works.

def createloans():
    #No way will I have time for 1 and 2.
    print("test")

def createloans2():
    print("Test")

def filtersearch():
    x = input("How many times do you want us to search?")
    print("loan_id","student_name","device_type","device_id","date_out","due_back","returned",)
    t = input("What do you want us to search for?")
    for x in loans:
        print(loans[x](t)) #Not working currently, working on it.



def deleteloan():
    print("Which loan do you want to delete?")
    print("0 - 4")
    print(loans[0])
    t = int(input())
    loans.pop(t)
    print("Loan deleted.")
    print(loans)
    



print("Welcome to the College Device Loan Manager!")
print("How can I help you?")
print("----------------------")
print("[1] View all Loans.")
print("[2] Create Loan")
print("[3] Create Loan (2)")
print("[4] Filter-Search")
print("[5] Update Loans")
print("[6] Delete Loan")
bit = input("Which function do you want to access?\n")
match(bit):
    case "View all Loans":
        viewallloans() #Works but doesn't get called(?)
    case "Update Loans":
        updateloan() # Working on it.
    case "Create Loan":
        createloans() # In Dev
    case "Create Loan (2)":
        createloans2() #In Dev
    case "Filter-Search":
        filtersearch() # In Dev
    case "Delete Loan":
        deleteloan() # Works

