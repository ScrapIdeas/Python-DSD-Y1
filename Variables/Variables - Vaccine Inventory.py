# Clinic vaccine stock (single brand for simplicity)
stock = 50

def dispense(stock, doses):
    stock = stock - doses
    print("Dispensed:", doses, "Remaining:", stock)

def restock(stock, amount):
    print("Before restock:", stock)
    stock = stock + amount
    print("After restock:", stock)

dispense(5)
restock(10)
print("End of day stock:", stock)
