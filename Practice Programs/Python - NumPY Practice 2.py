import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9,10])

print("from 1 to 5: ")
print(arr[1:5])
print("From 4 to the end:")
print(arr[4:])
print("From 9 to 8.")
print(arr[-3:-1])
print("From 2 to 4.")
print(arr[1:5:2])
print("Return every other element.")
print(arr[::2])
