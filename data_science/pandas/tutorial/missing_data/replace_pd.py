import pandas as pd
import numpy as np
from pandas import DataFrame

# replace function
print ("\n\n")
df = pd.read_csv('weather2.csv')
#df.replace([-99999], np.NaN, inplace=True)
df.replace({
    "temperature": -99999,
    "windspeed": -99999,
    "event": '0'
}, np.NaN, inplace=True)
print (df)

# example 2 - dict per value
print ("\n\n")
df = pd.read_csv('weather2.csv')
df.replace({
    -99999: np.NaN,
    '0': 'No Event'
}, inplace=True)
print (df)

# using regular expression
print ("\n\n")
df = pd.read_csv('weather2.csv')
df.replace({
    'temperature': '[A-Za-z]',
    'windspeed': '[A-Za-z]'
}, '', regex=True, inplace=True)
print (df)

# replace using a list of values
print ("\n\n")

df = DataFrame({
    'score': ['exceptional','average', 'good', 'poor', 'average', 'exceptional'],
    'student': ['rob', 'maya', 'parthiv', 'tom', 'julian', 'erica']
})

print (df)

print ('\n')
df.replace(['poor', 'average', 'good', 'exceptional'], [1,2,3,4], inplace=True)
print (df)