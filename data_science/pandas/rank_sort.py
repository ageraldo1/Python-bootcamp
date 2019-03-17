import numpy as np
import pandas as pd

from numpy.random import randn
from pandas import Series, DataFrame

ser1 = Series(range(3), index=list('CAB'))
ser1.sort_index() # sort by index
ser1.sort_values(ascending=False)      # sort by value

# rank
ser2 = Series(randn(10))
ser2  = ser2.sort_values()
print (ser2.rank())