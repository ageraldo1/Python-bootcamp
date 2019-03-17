import pandas as pd
import numpy as np
from pandas import DataFrame

df = pd.read_csv('weather.csv', parse_dates=['day'])

#df.set_index('day', inplace=True)
print (df)


# handle NaN for the entire dataset
print ("\n\n")
df.fillna(0, inplace=True)
print (df)

# handling NaN per column
print ("\n\n")
df = pd.read_csv('weather.csv', parse_dates=['day'])

df.fillna({
    'temperature': 0.0,
    'windspeed': 0.0,
    'event': 'no_event'
}, inplace=True)
print (df)


# using the previous value to fill a NaN
# bfill will you next value to replace current NaN value
print ("\n\n")
df = pd.read_csv('weather.csv', parse_dates=['day'])

df.fillna(method='ffill', inplace=True)
print (df)


# using interpolate
print ("\n\n")
df = pd.read_csv('weather.csv', parse_dates=['day'])

df.interpolate(method='linear', inplace=True)
print (df)


# using time to calculate the temperature diference - plot in a graph for details
print ("\n\n")
df = pd.read_csv('weather.csv', parse_dates=['day'])
df.set_index('day', inplace=True)
df.interpolate(method='time', inplace=True)
print (df)


# remove NaN 
print ("\n\n")
df = pd.read_csv('weather.csv', parse_dates=['day'])
df1 = df.dropna()
df2 = df.dropna(how='all')
df3 = df.dropna(thresh=2)
print (df1)


# reindex dataframe
print ("\n\n")
df = pd.read_csv('weather.csv', parse_dates=['day'])
df.set_index('day', inplace=True)
dt = pd.date_range('01-01-2017', '01-11-2017')
idx = pd.DatetimeIndex(dt)
df2 = df.reindex(idx)
print (df2)


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