import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# series
# same as an array but with labels
obj = Series([3,6,9,12])
print (obj)
print (obj.index)
print (obj.values)

# create a series
print ("\n\n")
www_cas =  Series([87, 43, 30, 21, 4], index=["USSR", "Germany", "China", "Japan", "USA"])
print (www_cas)
print (www_cas['USA'])

# check which countries had cas greater than 4
print ("\n\n")
print (www_cas[www_cas > 30])

# check 
print ("\n\n")
print ('BRA' in www_cas)

# convert a series to a dict
print ("\n\n")
www_dict = www_cas.to_dict()
print (www_dict)

# create a series based on a dict
www_new_series = Series(www_dict)

# using a list
countries =  ['China', 'Germany', 'Japan', 'USA', 'USSR', 'Argentina']
obj2 = Series(www_dict, index=countries)
print ("\n\n")
print (obj2)

print (pd.isnull(obj2))


# series adding - join series and add numbers
print ("\n\n")
new_series = www_cas + obj2
print (new_series)


# giving series names
print ("\n\n")
print ("\n\n")

obj2.name = 'World War 2 Casualities'
obj2.index.name = 'Countries'
print (obj2)
