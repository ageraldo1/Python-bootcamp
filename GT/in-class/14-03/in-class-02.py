import pandas as pd
from pandas import DataFrame

df = pd.read_csv('resources/movie_scores.csv')

#1 List all the columns in the data set.
print (df.columns)

# 2 We're only interested in IMDb data, so create a new table that takes the Film and all the columns relating to IMDB.
#df_imdb = 
#print (df['IMDB'])

df_imdb = df[['FILM', 'IMDB', 'IMDB_norm', 'IMDB_norm_round', 'IMDB_user_vote_count']]

# 3 Filter out only the good movies—i.e., any film with an IMDb score greater than or equal to 7 
# and remove the norm ratings.
df_good = df_imdb[df_imdb['IMDB'] >=7]

# check it
#df_good = df_imdb.loc[df_imdb['IMDB'] >=7, ['FILM', 'IMDB', 'IMDB_norm_round', 'IMDB_user_vote_count']]
#df_good = df_imdb.loc[df_imdb['IMDB'] >=7, :]


# 4 - Find less popular movies that you may not have heard about - i.e., anything with under 20K votes
#df_bad = df_imdb.loc[df_imdb['IMDB_user_vote_count'] <= 20000, :]

# 5 Finally, export this file to a spreadsheet, excluding the index, so we can keep track of our future watchlist.
#df.bad.to_excel('file.xlst', header=False)
