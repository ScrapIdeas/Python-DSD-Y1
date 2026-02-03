import matplotlib.pyplot as plt
import numpy as np

ListOfNumbers = [1,5,34,5,6,43,6,4,1,6,54,64,5,4]
z = 1
c = 9

plt.subplot(2,2,1)
plt.hist(ListOfNumbers)

plt.subplot(1,2,2)
plt.bar(z,c)

plt.show()
