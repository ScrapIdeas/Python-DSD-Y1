import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5] 
y1 = [2, 4, 6, 8, 10] 
y2 = [5, 3, 1, 7, 2] 

plt.plot(x,y1,y2)
plt.ylabel("Numbers")
plt.xlabel("More..Numbers.")
plt.title("Dual Axis Line Graph")
plt.show()