import pandas as pd
import random
from pandas import Series,DataFrame

# series
# one-dimentional 
# column and value(s)
# create one series for each dataframe column
price = Series([random.randrange(100) for i in range(5)]) 
review = Series([random.randrange(100) for i in range(5)]) 
product = Series(['Computer', 'Headset', 'Video-Game', 'Home-Theather', 'TV'])

#df = pd.concat([product,price,review], axis=1)
#print (d)

store = {
    'products': product,
    'price': price,
    'review': review,
    'stars': None
}

df = DataFrame(store)
print (df)