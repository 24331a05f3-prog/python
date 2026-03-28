import pandas as pd
data = {
    "Name": ["viswas", "raju", "yaswanth", "karthik", "satish"],
    "Marks": [74, 92, 78, 88, 95]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
df.loc[2, "Marks"] = None
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
df["Name"] = df["Name"].str.upper()
df["Result"] = df["Marks"].apply(lambda x: "Pass" if x >= 80 else "Fail")
df = df.rename(columns={"Marks": "Score"})
df["Bonus"] = df["Score"] + 5
print("\nModified & Cleaned DataFrame:")
print(df)