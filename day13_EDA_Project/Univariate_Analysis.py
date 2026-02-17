import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("housing.csv")

print("Skewness:", df["Price"].skew())
print("Kurtosis:", df["Price"].kurt())

plt.figure(figsize=(12,5))

plt.subplot(1,2,1)
sns.histplot(df["Price"], kde=True)
plt.title("Price Distribution")

plt.subplot(1,2,2)
sns.countplot(x=df["City"])
plt.title("City Count Plot")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

print("Most Frequent City:", df["City"].value_counts().idxmax())

