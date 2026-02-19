import numpy as np
import pandas as pd
np.random.seed(42)
data = np.random.normal(loc=170, scale=10, size=1000)
data = np.append(data, [120, 220, 250])
df = pd.DataFrame({"Values": data})
mean = df["Values"].mean()
std = df["Values"].std()
df["z_score"] = (df["Values"] - mean) / std
outliers = df[np.abs(df["z_score"]) > 3]
print("Mean:", round(mean, 2))
print("Standard Deviation:", round(std, 2))
print("\nOutliers (|Z| > 3):")
print(outliers)
import numpy as np
import pandas as pd
np.random.seed(42)
data = np.random.normal(loc=170, scale=10, size=1000)
data = np.append(data, [120, 220, 250])
df = pd.DataFrame({"Values": data})
mean = df["Values"].mean()
std = df["Values"].std()

df["z_score"] = (df["Values"] - mean) / std

outliers = df[np.abs(df["z_score"]) > 3]

print("Mean:", round(mean, 2))
print("Standard Deviation:", round(std, 2))
print("\nOutliers (|Z| > 3):")
print(outliers)
