import numpy as np
import pandas as pd

from pandas import Series, DataFrame

ser1 = Series(np.arange(3), index=['A', 'B', 'C'])
ser1 = 2*ser1
print ("\n ser1")
print (ser1)

# selecting by index name
print (ser1['B'])  # or ser1[1], ser[0:3], ser[['A', 'B']]

print (ser1[ser1 > 3])
ser1[ser1 > 3] = 10
print (ser1)


# dataframe
dframe = DataFrame(np.arange(25).reshape(5,5), index=['NYC', 'LA', 'SF', 'DC', 'Chi'], columns=['A', 'B', 'C', 'D', 'E'])
print ("\n dframe")
print (dframe)

# selecting data from a dataframe
# selecting one column
print (dframe['B'])   # multiple columns ['B', 'E']
print (dframe['C']>10)