import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

np.random.seed(42)

heights = np.random.normal(loc=170, scale=10, size=1000)
incomes = np.random.exponential(scale=50000, size=1000)
scores = np.random.beta(a=5, b=1, size=1000) * 100

data = pd.DataFrame({
    "Heights": heights,
    "Incomes": incomes,
    "Scores": scores
})

fig, axes = plt.subplots(3, 1, figsize=(10, 15))

datasets = [
    ("Heights", "Normal Distribution - Human Heights"),
    ("Incomes", "Right-Skewed Distribution - Household Income"),
    ("Scores", "Left-Skewed Distribution - Easy Exam Scores")
]

for ax, (column, title) in zip(axes, datasets):
    mean = data[column].mean()
    median = data[column].median()
    
    sns.histplot(data[column], kde=True, bins=30, ax=ax)
    
    ax.axvline(mean, color='red', linestyle='--', linewidth=2, label=f"Mean = {mean:.2f}")
    ax.axvline(median, color='green', linestyle='-', linewidth=2, label=f"Median = {median:.2f}")
    
    ax.set_title(title)
    ax.legend()
    
    print("=========================================")
    print(title)
    print("Mean   :", round(mean, 2))
    print("Median :", round(median, 2))
    
    if mean > median:
        print("Distribution Type: Right-Skewed")
    elif mean < median:
        print("Distribution Type: Left-Skewed")
    else:
        print("Distribution Type: Normal (Symmetric)")
    print("=========================================\n")

plt.tight_layout()
plt.show()
