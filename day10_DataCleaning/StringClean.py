import pandas as pd
data = {
    "CustomerID": [1, 2, 3, 4, 5],
    "Location": ["New York", " new york", "NEW YORK ", "New york", " new YORK "]
}
df = pd.DataFrame(data)
#Check unique values BEFORE cleaning
print("Before Cleaning:")
print(df["Location"].unique())

df["Location"] = df["Location"].str.strip()
df["Location"] = df["Location"].str.title()
#Verify fix using unique()
print("\nAfter Cleaning:")
print(df["Location"].unique())

print("\nUpdated DataFrame:")
print(df)
