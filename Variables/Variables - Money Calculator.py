username = input("Enter your name.")
MobilePhoneNetwork = input("Enter Your Mobile Phone Network.")
MinutesUsedThisMonth = input("What amount of minutes did you use?")
TotalMinutes = int(MinutesUsedThisMonth) * 0.10
TotalTexts = input("Amount of texts you have sent in a month?")
#Better be safe than sorry, putting in Int for now.
TotalTotalTexts = int(TotalTexts) * 0.05 
TotalBill = TotalTotalTexts + TotalMinutes
print("Your total bill amounts to: ", TotalBill, "\n")
TotalBill = TotalBill + (TotalBill % 20)
print("Your total bill with tax, amounts to: ", TotalBill, "\n")
