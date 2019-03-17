import pandas as pd
from pandas import DataFrame,Series

shop = {
    "Frame": ['Ballon', 'Concrete', 'Space', 'Portal', 'Braced'],
    "Price": [50.5, 100.30, 70.00, 80.00, 90.00],
    "Sales": [100, 5000, 845, 948, 400]
}

df = DataFrame(shop)
print ("\n Shop Dataframe")
print (df)

gallery =  Series(['Picasso', 100, 100], index=["Paiting", "Price", "Popularity"])
df2 = DataFrame(gallery)

print ("\n Art Gallery")
print (df2)


print ("\n")

artist =  Series(['Picasso', 'Van Gogh', 'Toddler'])
price = Series([300, 400, 1000])

df3 = DataFrame([artist, price], columns=['Paiting', 'Price'])
print (df3)
