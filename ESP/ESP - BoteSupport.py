import pandas as pd
import csv
import matplotlib.pyplot as plt

# Outputs the initial menu and validates the input
def main_menu():
    flag = True

    while flag:

        print("####################################################")
        print("############# Botes Parcels CRM System #############")
        print("####################################################")
        print("")
        print("########### Please select an option ################")
        print("### 1. Total issues by type")

        choice = input('Enter your number selection here: ')

        if(choice != '1'): #Checks whether the input was 1, and if it wasn't, it prompts the user again.
            print("Sorry, you did not enter a valid option")
            flag = True #Sets the flag to true to keep it going.
        elif(choice == '1'): #IF the input is 1, then it goes further.
            print('Choice accepted!')  
            flag = False #Sets the flag to false to go further with the program.

    return choice

  # Submenu for totals, provides type check validation for the input and returns issue type as a string
def total_menu():
    flag = True

    while flag:

        print("####################################################")
        print("############## Total issues by type ################")
        print("####################################################")
        print("")
        print("########## Please select an issue type ##########")
        print("### 1. Customer Account Issue")   
        print("### 2. Delivery Issue") 
        print("### 3. Collection Issue")  
        print("### 4. Service Complaint")

        choice = input('Enter your number selection here: ')

        try:
            int(choice)
        except:
            print("Sorry, you did not enter a valid option")
            flag = True
        else:    
            print('Choice accepted!')
            choice = int(choice)
            flag = False

    issueTypeList = ["Customer Account Issue", "Delivery Issue", "Collection Issue", "Service Complaint"]
    

    issueType = issueTypeList[choice]
  
    return issueType     

# Creates a new dataframe then counts the number of occurences of the requested issue type

def get_total_data(total_menu_choice):
    
    issues = pd.read_csv("Task4a_data.csv")
    
    total = issues['Issue Type'].value_counts()[total_menu_choice]

    msg = "The total number of issues logged as a {} was: {}".format(total_menu_choice, total)
    df = pd.DataFrame(issues[['Region','Issue Type','How Resolved']]) # Used separately, it uses the open csv to filter out specific columns.
    dt = pd.DataFrame(issues) #Used as the main source for the Dataframe, pulls from issues, or the CSV in other words.

    plt.xlabel('Issue Type') #Used for the bar chart.
    plt.ylabel('Days To Resolve') 
    
    plt.bar(dt['Issue Type'],dt['Days To Resolve'], width=0.4) #Pulls required information from dt, which is used as the main source for the dataframe and then plots it as a graph.
    plt.show()                                                 #P.s, would've worked on the top thing since It's all 4s, however I was left with figuring out how Matplotlib works with the abhorrid abomination that is Pandas, so regardless what you think, this is a win for me.

    df.head(5)
    print(df)
    return msg



main_menu_choice = main_menu()
if main_menu_choice ==  '1': #Changed the '1' to a string, so when it retrieves the choice from the main_menu, it starts.. the function.
    total_menu_choice = total_menu()
    print(get_total_data(total_menu_choice))

  

