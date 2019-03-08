import numpy as np

# Universal Functions
arr = np.arange(11)
print (f"Original array    : {arr}")
print (f"Square root array : {np.sqrt(arr)}")
print (f"Exponential array : {np.exp(arr)}")



# binary functions
A = np.random.randn(10)
B = np.random.randn(10)

print (f"Original A array  : {A}")
print (f"Original B array  : {B}")
print (f"Adding two arrays : {np.add(A,B)}")
print (f"Max two arrays    : {np.maximum(A,B)}")
print (f"Min two arrays    : {np.minimum(A,B)}")
