import numpy as np

# create a array based on a list
my_list1 = [1,2,3,4]
my_array1 = np.array(my_list1)

print (my_array1)
print (type(my_array1))

my_list2 = [11, 22, 33, 44]
my_join_list = [my_list1, my_list2]

# create a matrix ( 2 x 4)
# each new list create a new row
my_array2 = np.array(my_join_list)
print (my_array2)

# array shape
print ( f"Array shape : {my_array2.shape}")
print ( f"Array Type  : {my_array2.dtype}")
print ("\n")

# create zero, ones, empty arrays or vectors
print (f"Zero vector of 5 elements  : {np.zeros(5)}")
print (f"Zero datatype              : {np.zeros(5).dtype}")
print (f"Ones matrix of 5 x 5       : {np.ones([5,5])}")
print (f"Ones datatype              : {np.ones([5,5]).dtype}")
print (f"Empty vector of 5 elements : {np.empty(5)}")
print (f"Empty datatype             : {np.empty(5).dtype}")


# identity matrix
print (f"Identity matrix 2 x 2       :\n {np.eye(2)}")

# matrix/vector by range
print (f"Vector with 5 elements                 : {np.arange(5)}")
print (f"Vector start at 5, 50 elements, step 2 : {np.arange(5,50,2)}")


