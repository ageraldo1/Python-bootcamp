import numpy as np
import pandas as pd

from pandas import Series, DataFrame
import webbrowser

website = 'http://en.wikipedia.org/wiki/NFL_win-loss_records'
#webbrowser.open(website)

nfl_frame = pd.read_clipboard()
print (nfl_frame)

# columns names
print ( nfl_frame.columns)
print (nfl_frame.Rank)
print (nfl_frame["First NFL Season"])

df1 = DataFrame(nfl_frame, columns=['Rank', 'Team', 'Not_Exits_Column'])
print ("\n\n\t df1")
print (df1)    


# head / tail
print ("\n\n")
print (nfl_frame.head(1))
print (nfl_frame.tail(1))


# retrieve rows
print ("\n\n")
print (nfl_frame.iloc[3])
#print (nfl_frame.loc['Team'] == 'Dallas Cowboys')

# change columns values
#print (nfl_frame['Stadium'] = 'Itaquerao')

# Add new series
states = Series(['GA', 'NY', 'PX', 'TL', 'MA', 'MO'])
print (states)

nfl_frame['States'] = states
print ("\n\n")
print (nfl_frame)

# delete columns / series
del nfl_frame['States']


# create a dataframe based on a dict obj
print ("\n\n")
data = {
    'City': ['Suwanee', 'Cumming', 'New York'],
    'Population': [83,97,1385]
}

city_frame = DataFrame(data)
print (city_frame)