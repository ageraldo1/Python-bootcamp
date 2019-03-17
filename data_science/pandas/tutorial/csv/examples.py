import pandas as pd
from pandas import DataFrame


df = pd.read_csv('../dataframes/weather_data.csv')

# check converters !!! powerful!

print (df.columns)

# write to csv
df.to_csv('new.csv', index=False, columns=['day', 'temperature', 'windspeed', 'event'], header=True)
df.to_excel('new.xlsx')

# check also pd.ExcelWriter
#pd.ExcelWriter()