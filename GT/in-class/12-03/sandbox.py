import pandas as pd
import random
from pandas import Series,DataFrame

ser1 = Series([[random.randrange(100) for i in range(3)]])
#ser2 = Series([random.randrange(100) for i in range(10)])
#ser3 = Series([random.randrange(100) for i in range(10)])

df1 = DataFrame(dict(ser1))
print (df1)