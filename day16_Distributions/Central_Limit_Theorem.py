import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
np.random.seed(42)
original_data = np.random.exponential(scale=50000, size=10000)
sample_means = []

for i in range(1000):
    sample = np.random.choice(original_data, size=30)
    sample_means.append(np.mean(sample))
sample_means = pd.Series(sample_means)

plt.figure(figsize=(8,5))
sns.histplot(sample_means, kde=True, bins=30)
plt.title("Distribution of Sample Means (n=30, 1000 samples)")
plt.xlabel("Sample Mean")
plt.ylabel("Frequency")
plt.show()
print("Original Data Mean:", round(np.mean(original_data), 2))
print("Mean of Sample Means:", round(sample_means.mean(), 2))
