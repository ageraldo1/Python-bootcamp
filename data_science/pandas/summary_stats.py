import numpy as np
import pandas as pd

from pandas import Series, DataFrame

arr = np.array([[1,2, np.nan], [np.nan, 3,4]])
df1 = DataFrame(arr, index=['A', 'B'], columns=['One', 'Two', 'Three'])

# sum of columns
print (df1)
print (df1.sum()) # sum by column
print (df1.sum(axis=1)) # sum by row

# min/max
print (df1.min()) # return the min value for each column
print (df1.min(axis=1)) # return the min value for each row
print (df1.idxmin()) # return the index column instead

# stats
print (df1.describe())

