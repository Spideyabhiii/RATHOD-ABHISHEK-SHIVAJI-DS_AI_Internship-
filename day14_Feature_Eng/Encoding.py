import pandas as pd
data = {
    'Transmission': ['Automatic', 'Manual', 'Automatic', 'Manual'],
    'Color': ['Red', 'Blue', 'Green', 'Red']
}

df = pd.DataFrame(data)
print("Original Dataset:\n")
print(df)
# Step 2: Label Encoding (Transmission)
# Since Transmission is binary (Automatic/Manual)
df['Transmission'] = df['Transmission'].map({
    'Manual': 0,
    'Automatic': 1
})
print("\nAfter Label Encoding (Transmission):\n")
print(df)
# Step 3: One-Hot Encoding (Color)
# Since Color is nominal (no order)
df = pd.get_dummies(df, columns=['Color'], drop_first=True)
print("\nFinal Encoded Dataset:\n")
print(df)
