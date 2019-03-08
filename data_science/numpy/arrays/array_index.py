import numpy as np

arr = np.arange(0,11)

# index access
print (arr[10])

# index range
print (arr[1:5])
print (arr[0:5])

# set values
arr[0:5] = 100
print (arr)

# reset array
arr = np.arange(0,11)

# slice
print ("\b\b")
slice_of_arr = arr[0:6]
print (f"Original array : {arr}")
print (f"Sliced array   : {slice_of_arr}")

# changing all elements
# attention in this case - slice does not copy the array data!
# use the method arr.copy instead to copy your original array to a new array object
slice_of_arr[:] = 99
print (f"Original array : {arr}")
print (f"Sliced array   : {slice_of_arr}")


# matrix
arr_2d = np.array(([5,10,15],[20,25,30],[35,40,45]))
print (f"Matrix 3 x 3 \n {arr_2d}")

print (f"Row 0 : {arr_2d[0]}")
print (f"Row 1 : {arr_2d[1]}")
print (f"Row 1, column 2: {arr_2d[1,2]}")

# 2d slicing
arr_2d_slice = arr_2d[:2,1:]
print (f"Sliced array \n {arr_2d_slice}")

# facing indexing
fancy_arr = np.zeros((10,10))
print (f"Facing array \n {fancy_arr}")
print (f"Array length \n {fancy_arr[[2,4,5]]}")