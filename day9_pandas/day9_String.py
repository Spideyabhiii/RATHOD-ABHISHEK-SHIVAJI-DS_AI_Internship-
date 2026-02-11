import pandas as pd

# Create Series
usernames = pd.Series([' Alice ', 'bOB', 'Charlie_Data ', 'daisy'])

# Remove spaces and convert to lowercase
cleaned = usernames.str.strip().str.lower()

print("Cleaned Usernames:")
print(cleaned)

# Check names containing letter 'a'
contains_a = cleaned.str.contains('a')

print("\nNames Containing 'a':")
print(contains_a)
