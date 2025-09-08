import pandas as pd

data = pd.read_excel("Education.xlsx")
print(data.head())

print(data.tail())

print(data.iloc[2,])

print(data.shape)