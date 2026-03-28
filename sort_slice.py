import pandas as pd

data = {
    "Name": ["viswas", "raju", "yaswanth", "karthik", "satish"],
    "Marks": [85, 92, 78, 88, 95]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

sorted_df = df.sort_values(by="Marks")
print("\nSorted by Marks (Ascending):")
print(sorted_df)

sorted_desc = df.sort_values(by="Marks", ascending=False)
print("\nSorted by Marks (Descending):")
print(sorted_desc)

print("\nFirst 3 rows:")
print(df.iloc[:3])

print("\nRows 1 to 3 and columns Name & Marks:")
print(df.loc[1:3, ["Name", "Marks"]])

