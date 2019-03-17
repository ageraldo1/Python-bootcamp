import numpy as np
import pandas as pd

from pandas import Series, DataFrame

# adding series
ser1 = Series([0,1,2], index=['A', 'B', 'C'])
ser2 = Series([3,4,5,6], index=['A', 'B', 'C', 'D'])

ser3 = (ser1 + ser2)
print (ser3)


# adding dataframes
df1 = DataFrame(np.arange(4).reshape(2,2), columns=list('AB'), index=['NYC', 'LA'])
df2 = DataFrame(np.arange(9).reshape(3,3), columns=list('ADC'), index=['NYC', 'SF', 'LA'])
#df3 = df1 + df2
df3 = df1.add(df2, fill_value = 0)
print (df3)

ser3 = df2.iloc[0]  #  df2.loc['LA']
print (df2 - ser3)