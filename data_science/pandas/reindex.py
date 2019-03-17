import numpy as np
import pandas as pd

from pandas import Series, DataFrame
from numpy.random import randn

ser1 = Series([1,2,3,4], index=['A', 'B', 'C', 'D'])
ser2 = ser1.reindex(['A', 'B', 'C', 'D', 'E', 'F'])

print ("\n Series 1")
print (ser1)

print ("\n Series 2")
print (ser2)

# filling the null values
ser3 = ser2.reindex(['A', 'B', 'C', 'D', 'E', 'F', 'G'], fill_value=0)
print ("\n Series 3")
print (ser3)

#
ser4 = Series(['USA', 'Mexico', 'Canada'], index=[0,5,10])
ranger = range(15)
ser5 = ser4.reindex(ranger, method='ffill')
print ("\n Series 4")
print (ser4)
print (ser5)


# reindex dataframe
dframe = DataFrame(randn(25).reshape(5,5), index=['A', 'B', 'D', 'E', 'F'], columns=['c1', 'c2', 'c3', 'c4', 'c5'])
print (print ("\n DFrame "))
print (dframe)

print (print ("\n DFrame2 "))
dframe2 = dframe.reindex(['A', 'B', 'C', 'D', 'E', 'F'])
print (dframe2)


# reindex columns
new_columns = ['col1', 'col2', 'col3', 'col4', 'col5', 'col6']
dframe3 = dframe2.reindex(columns=new_columns)
print (print ("\n DFrame3 "))
print (dframe3)






# reindex in place
print (print ("\n DFrame "))
print (dframe)

#dframe.
#dframe.ix(['A', 'B', 'C', 'D', 'E', 'F'], new_columns])
#print (dframe)

