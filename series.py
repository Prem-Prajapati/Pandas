import numpy as np
import pandas as pd
a = pd.Series([1,2,3,4,5])
print(a)

#with index
b = pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
print(b)

stat_dict = {'Pencil':10,
             'Eraser':20,
             'Sharpner':15}
print(pd.Series(stat_dict))

arr = np.array(['q','w','e','r','t'])
index = [1,2,3,4,5]
arr1 = pd.Series(arr,index=index)
print(arr1)
print(a.describe())