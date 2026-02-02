import matplotlib.pyplot as plt
import numpy as np 

data = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]) 
plt.imshow(data)
plt.title("Heatmap")
plt.xlabel("This is the Label for X Axis")
plt.ylabel("Label for Y-axis")
plt.colorbar()
plt.show()