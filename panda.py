import pandas as pd
df = pd.read_csv("C:\\Users\\Asus\\Downloads\\students.csv")
print(df.head())
print(df.tail())
print(df.info())

print(df.describe())
