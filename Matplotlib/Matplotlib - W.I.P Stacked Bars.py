import matplotlib.pyplot as plt
labels = ['Group A', 'Group B'] 
data = [[10, 20], [5, 15]] 
plt.bar(data, stacked = True, labels = labels)
plt.show()