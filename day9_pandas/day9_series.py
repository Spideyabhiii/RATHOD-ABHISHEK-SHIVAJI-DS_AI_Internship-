import pandas as pd
# Create Series with custom labels
products = pd.Series([700, 150, 300], 
                     index=['Laptop', 'Mouse', 'Keyboard'])
# Print full Series
print("Full Series:")
print(products)
# Access price of Laptop
print("\nPrice of Laptop:")
print(products['Laptop'])
# Slice first two products
print("\nFirst Two Products:")
print(products.iloc[0:2])
