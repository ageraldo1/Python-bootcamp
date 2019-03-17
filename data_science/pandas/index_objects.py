import numpy as np
import pandas as pd
from pandas import Series, DataFrame

my_series = Series([1,2,3,4], index=['A', 'B', 'C', 'D'])

print ("\nSeries output")
print (my_series)

print ("\nIndex output")
print (my_series.index)

print ("\nIndex value")
print (my_series.index[2])
print (my_series.index[2:])

