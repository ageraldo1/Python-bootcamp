import pandas as pd
from pandas import DataFrame

df = pd.read_csv('weather_data.csv')
#print (df)

# print shape
#print (df.shape)    # rows x columns


# slice
#print (df[2:5])

# min/max/mean/std
#print (df['temperature'].max())
#print (df.describe(include ='all'))
#print (df.info())

# filter
# select all rows in the dataframe
# df[]
# where temperature > 32
# df[df['temperature'] > 32]
#print (df[df['temperature'] >= 32])

#print (df[df['temperature'] == df['temperature'].max()])

# select only day and apply the same filter
print(df['day'][df['temperature'] == df['temperature'].max()])

print(df[['day', 'temperature']][df['temperature'] == df['temperature'].max()])

# index
print (df.index)
df.set_index('day', inplace=True)
print ("\n\n")
print (df)
print ("\n\n")
print (df.loc['1/4/2017'])  # search by index value

df.reset_index(inplace=True)
print ("\n\n")
print (df)

# using a tuple to create a DataFrame
weather_data = [
    ('01/01/2017', 100, 'Sunny'),
    ('02/01/2017', 80, 'Cold'),
    ('03/01/2017', 40, 'Frozen')
]

df = DataFrame(weather_data, columns=['Date', 'temperature', 'Weather'])
print (df)