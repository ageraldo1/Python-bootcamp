import pandas as pd
from pandas import DataFrame


#1 Read in the csv using Pandas and print out the DataFrame that is returned
df = pd.read_csv('resources/crime_incident_data2017.csv')
print (df.head(5))

#2 Get a count of rows within the DataFrame in order to determine if there are any null values
print (df.info())
print (df.nunique(dropna=False))
#print (df.count())

# 3 Drop the rows which contain null values
df.dropna(inplace=True, how='any')
print (df.info())

# 4 Search through the "Offense Type" column and 
# replace any similar values with one consistent value
print(df['Offense Type'].value_counts())

df['Offense Type'].replace({
        "Vandalism": "Burglary"
    }, inplace=True)

print ('\n\n')
print(df['Offense Type'].value_counts())    

# 5 Create a couple DataFrames that look into one Neighborhood only and print them to the screen
#print(df['Neighborhood'].value_counts())
df_nh = df[df['Neighborhood'] == 'Homestead']
print (df_nh.head(5))
print (df_nh.count())

# same thing
#df_nh_loc = df.loc[df['Neighborhood']== 'Homestead']
#print (df_nh_loc.count())