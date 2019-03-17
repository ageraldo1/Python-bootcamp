import pandas as pd
from pandas import DataFrame

df = pd.read_csv('weather.csv')
g = df.groupby('city')

for city, city_df in g:
    print (f'\n{city}')
    print (f'{city_df}')

# selecting a specific group
print ('\n\n')
g_paris = g.get_group('paris')
print (g_paris)    
print (g_paris.describe())

# applying stats functions against the group
# split / apply / combine
print ('\n\n')
print (g.max()) # all fields
print (g['temperature'].max())  # just one field
print (g.count())  # just one field
print (g.mean())

print ('\n\n')
print (g.describe())

# to plot
# %pylab
# g.plot()
