import pandas as pd

# using default values
g_play = pd.read_csv('resources/googleplaystore.csv')
#print(g_play.head(5))

# passing file delimiter
g_play = pd.read_csv('resources/googleplaystore.csv', sep=',')
#print(g_play.head(5))

# limiting the number of rows
g_play = pd.read_csv('resources/googleplaystore.csv', sep=',', nrows=20)
#print (g_play)

# removing the header
g_play = pd.read_csv('resources/googleplaystore.csv', sep=',', nrows=20, header=None)
#print (g_play)

# change columns header name
c_name = ['App', 'Category', 'Rating', 'Reviews', 'Size', 'Installs', 'Type', 'Price', 'Content Rating', 'Genres', 'Last Updated', 'Current Ver', 'Android Ver']
g_play = pd.read_csv('resources/googleplaystore.csv', sep=',', nrows=20, header=None, names=c_name)
print (g_play)

# loading Excel 
#g_play = pd.read_excel('excel_file',0)
