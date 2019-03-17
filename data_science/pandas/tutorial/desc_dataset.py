import pandas as pd
from pandas import DataFrame

csv_source = 'resources/googleplaystore.csv'

g_play = pd.read_csv(csv_source)

# only numberic values by default
#print (g_play.describe())

# all columns
#print (g_play.describe(include ='all'))

# only string data
#print (g_play.describe(include =['object']))

# only float data
#print (g_play.describe(include =['float']))

# filtering dataframe
#print (g_play[['Rating', 'Reviews']])
print(g_play[(g_play['Rating'] > 4.9)].describe())
print(g_play[(g_play['Category'] == 'ART_AND_DESIGN')].describe())
print(g_play.info())


#g_play[column][filter]