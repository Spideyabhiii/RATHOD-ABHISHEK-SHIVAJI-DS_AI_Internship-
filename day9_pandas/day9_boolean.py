import pandas as pd
# Create Series
grades = pd.Series([85, None, 92, 45, None, 78, 55])

print("Original Series:")
print(grades)

print("\nMissing Values:")
print(grades.isnull())

filled_grades = grades.fillna(0)

print("\nFilled Series:")
print(filled_grades)

filtered = filled_grades[filled_grades > 60]

print("\nScores Greater Than 60:")
print(filtered)
