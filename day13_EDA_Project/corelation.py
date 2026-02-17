import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("housing.csv")

corr = df.corr(numeric_only=True)
print("Correlation Matrix:\n")
print(corr)

print("\nHighly Correlated Pairs (>|0.8|):")

found = False
for i in corr.columns:
    for j in corr.columns:
        if i < j and abs(corr.loc[i, j]) > 0.8:
            print(f"{i} and {j} -> {corr.loc[i, j]}")
            found = True

if not found:
    print("No highly correlated pairs found.")

plt.figure(figsize=(12,5))

# Heatmap
plt.subplot(1,2,1)
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")

# Boxplot (Outlier Detection)
plt.subplot(1,2,2)
sns.boxplot(y=df["Price"])
plt.title("Boxplot of Price (Outliers)")

plt.tight_layout()
plt.show()

print("\nObservation: Heatmap shows relationships between variables.")
print("Boxplot highlights potential outliers in Price.")
