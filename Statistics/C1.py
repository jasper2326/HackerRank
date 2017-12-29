from pandas import Series, DataFrame
import pandas as pd

obj = Series([4, 7, -5, 3])
print(obj)
print(obj.values)
print(obj.index)

obj2 = Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
print(obj2)
print(obj2.index)


