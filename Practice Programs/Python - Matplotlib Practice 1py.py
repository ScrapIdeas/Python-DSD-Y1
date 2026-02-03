import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0,10,0.2)
y = np.sin(x)
plt.ylim(-2,2)

#Reverting the changes
ax = plt.gca() # - Get current axis.
ax.set_ylim(-1,1)

plt.plot(x,y)
plt.show()