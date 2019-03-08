import numpy as np

arr = np.arange(50).reshape((10,5))

# interchange rows and columns
# first row become first column
# second row become second column
print (f"Original array \n {arr}")
print (f"\nTranspose array \n {arr.T}")

print (f"\nDot Product \n {np.dot(arr.T, arr)}")

arr3d = np.arange(50).reshape((5,5,2))
print (f"3d array \n {arr3d}")

# swap axes
arr = np.array([[1,2,3]])
print (f"Original array \n {arr}")
print (f"\nSwap array \n {arr.swapaxes(0,1)}")

