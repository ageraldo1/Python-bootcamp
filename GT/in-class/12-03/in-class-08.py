import pandas as pd
from pandas import Series, DataFrame

show = {
    "Character_in_show": ['Arnold', 'Gerald', 'Helga', 'Phoebe', 'Harold', 'Eugene'],
    "color_of_hair": ['blonde', 'black', 'blonde', 'black', 'unknown', 'red'],
    "Height": ['average', 'tallish', 'tallish', 'short', 'tall', 'short'],
    "Football_Shaped_Head": [True, False, False, False, False, False]
}

df1 = DataFrame(show)
print (f"DF1 \n {df1}")

df2 = df1.rename(columns= {"Character_in_show": "Character", "color_of_hair": "Hair Color", "Football_Shaped_Head": "Football Head"})
print (f"DF2 \n {df2}")

df3 = df2[['Character', 'Football Head', 'Hair Color', 'Height']]
print (f"DF3 \n {df3}")