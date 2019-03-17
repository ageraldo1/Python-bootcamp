import numpy as np
import pandas as pd

from pandas import Series, DataFrame

ser1 = Series(np.arange(3), index=['a', 'b', 'c'])
print ("\n ser1")
print (ser1)

print ("\n")
print(ser1.drop('b'))


# df
df1 = DataFrame(np.arange(9).reshape(3,3),index=['SP', 'RJ', 'DF'], columns=['Population', 'Size', 'Houses'])
print ("\n df1")
print (df1)

# print drop row
print (df1.drop('SP'))  # default axis[0]

# drop column
print (df1.drop('Houses', axis=1))   # axis[0] = rows, axis[1] = columns
