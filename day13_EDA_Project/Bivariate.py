import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("housing.csv")

plt.figure(figsize=(12,5))

# Scatter plot
plt.subplot(1,2,1)
sns.scatterplot(x=df["Area_sqft"], y=df["Price"])
plt.title("Area vs Price")

# Boxplot
plt.subplot(1,2,2)
sns.boxplot(x=df["City"], y=df["Price"])
plt.xticks(rotation=45)
plt.title("City vs Price")

plt.tight_layout()
plt.show()
