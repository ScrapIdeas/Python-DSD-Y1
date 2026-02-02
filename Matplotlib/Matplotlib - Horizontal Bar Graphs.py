import matplotlib.pyplot as plt
x = ['A', 'B', 'C', 'D', 'E'] 
y = [10, 5, 8, 6, 12] 

plt.barh(x,y)
plt.xlabel("Numbers")
plt.ylabel("Letters")
plt.title("A Horizontal Bar Graph")
plt.show()