import pandas as pd
data = {
    "ProductID": [1, 2, 3, 4],
    "ProductName": ["Laptop", "Mouse", "Keyboard", "Monitor"],
    "Price": ["$750.00", "$25.50", "$45.99", "$199.99"],  # stored as string
    "Date": ["2026-01-01", "2026-01-03", "2026-01-05", "2026-01-07"]  # stored as object
}
df = pd.DataFrame(data)
# Check initial data types
print("Before Conversion:\n")
print(df.dtypes)
#Remove '$' and convert Price to float
df["Price"] = df["Price"].str.replace("$", "", regex=False).astype(float)
#Convert Date to datetime
df["Date"] = pd.to_datetime(df["Date"])
#Check final data types
print("\nAfter Conversion:\n")
print(df.dtypes)
#Display updated DataFrame
print("\nUpdated DataFrame:\n")
print(df)
