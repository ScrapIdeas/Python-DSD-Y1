import matplotlib.pyplot as plt
import time

Arrays = "RandomStuff, WeirderStuff"
RandomStuff = [5,4,3,5,1,6,4,5]
WeirderStuff = [100,1000,10000,10000,100000] 
ch = True
while(ch == True):
    d = input(f"Which array do you want: {Arrays}\n")
    match (d):
        case "RandomStuff":
            d = RandomStuff
            ch = False
        case "WeirderStuff":
            d = WeirderStuff
            ch = False

plt.ylabel("The Histogram")
plt.xlabel()
plt.hist(d)
plt.grid()
plt.show()