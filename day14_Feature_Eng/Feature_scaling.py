import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, MinMaxScaler
data = {
    'Age': [22, 25, 30, 35, 40],
    'Salary': [20000, 25000, 30000, 40000, 50000]
}
df = pd.DataFrame(data)
# Standardization
scaler_standard = StandardScaler()
df_standardized = pd.DataFrame(
    scaler_standard.fit_transform(df),
    columns=df.columns
)
# Normalization
scaler_minmax = MinMaxScaler()
df_normalized = pd.DataFrame(
    scaler_minmax.fit_transform(df),
    columns=df.columns
)
# One Output with 3 Histograms
plt.figure()
plt.subplot(1, 3, 1)
plt.hist(df['Salary'], bins=5)
plt.title("Original")

plt.subplot(1, 3, 2)
plt.hist(df_standardized['Salary'], bins=5)
plt.title("Standardized")

plt.subplot(1, 3, 3)
plt.hist(df_normalized['Salary'], bins=5)
plt.title("Normalized")

plt.tight_layout()
plt.show()
