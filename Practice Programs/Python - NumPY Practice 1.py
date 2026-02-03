import numpy as np

arr = np.array([1,2,3,4,5]) # Normal array in NumPY

arrtup = np.array((1,2,3,4,5)) # Array using Tuples in NumPY

arrD = np.array(42) # 0-D Array in NumPY

Arr2d = np.array([[1, 2, 3], [4, 5, 6]]) # Array that's two dimensional or something

print(arr)
print(Arr2d)
print(arrD)
print(arrtup)

print(f"The Dimension for this array is: {Arr2d.ndim}, Array: Arr2d") #Used to check dimensions
print(type(arr)) #Used to check types