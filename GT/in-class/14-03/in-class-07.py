import pandas as pd

# 1 Read the Pokemon CSV file with Pandas.
df = pd.read_csv('resources/pokemon.csv')

# 2 Create a new table by extracting the following columns: "Type 1", "HP", "Attack", "Sp. Atk", "Sp. Def", and "Speed".
df_p = df[['Type 1', 'HP', 'Attack', 'Sp. Atk', 'Sp. Def', 'Speed']]
print (df_p.columns)
print (df_p.head(5))

# 3 Find the average stats for each type of Pokemon.
print(df_p.groupby('Type 1').mean())

# 4 Create a new DataFrame out of the averages.
df_avg = df_p.groupby('Type 1').mean()

# 5 Calculate the total power level of each type of Pokemon 
# by adding all of the previous stats together and place the results into a new column.
print ("\n\n")
#print (df_avg.groupby('Type 1')['Bug'])
#print (df_avg.groupby('Type 1').sum())
#total = df_avg[''

for k,v in df_avg.iterrows():
    print (f'{k} - {sum(v)}')
