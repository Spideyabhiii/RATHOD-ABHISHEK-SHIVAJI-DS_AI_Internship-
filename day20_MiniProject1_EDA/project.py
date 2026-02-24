# MINI PROJECT 1 – EXPLORATORY DATA ANALYSIS (EDA)
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="whitegrid")
# PHASE 1 – DATASET INSPECTION
print("\n==============================")
print("PHASE 1 – DATASET INSPECTION")
print("==============================")
df = pd.read_csv("titanic.csv")
print("\nFirst 5 Rows:")
print(df.head())
print("\nDataset Information:")
df.info()
print("\nStatistical Summary:")
print(df.describe())
# PHASE 2 – DATA CLEANING
# ==============================
print("\n==============================")
print("PHASE 2 – DATA CLEANING")
print("==============================")
print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())
# Drop Cabin column
if 'Cabin' in df.columns:
    df = df.drop(columns=['Cabin'])
# Fill missing values properly (no inplace error)
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
# Remove duplicates
df = df.drop_duplicates()
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())
# ==============================
# PHASE 3 – CLEAN VISUAL DASHBOARD
# ==============================

print("\n==============================")
print("VISUAL DASHBOARD")
print("==============================")

fig = plt.figure(figsize=(22,12))
plt.subplots_adjust(hspace=0.35, wspace=0.30)

# 1️⃣ Age Distribution
ax1 = plt.subplot(2,3,1)
sns.histplot(df['Age'], kde=True)
ax1.set_title("Age Distribution", fontsize=13)
ax1.set_xlabel("Age")
ax1.set_ylabel("Count")

# 2️⃣ Passenger Class Distribution
ax2 = plt.subplot(2,3,2)
sns.countplot(x='Pclass', data=df)
ax2.set_title("Passenger Class Distribution", fontsize=13)
ax2.set_xlabel("Passenger Class")
ax2.set_ylabel("Count")

# 3️⃣ Survival Count
ax3 = plt.subplot(2,3,3)
sns.countplot(x='Survived', data=df)
ax3.set_title("Survival Count", fontsize=13)
ax3.set_xlabel("Survived (0 = No, 1 = Yes)")
ax3.set_ylabel("Count")

# 4️⃣ Survival by Gender
ax4 = plt.subplot(2,3,4)
sns.countplot(x='Sex', hue='Survived', data=df)
ax4.set_title("Survival by Gender", fontsize=13)
ax4.set_xlabel("Gender")
ax4.set_ylabel("Count")

# 5️⃣ Age vs Survival
ax5 = plt.subplot(2,3,5)
sns.boxplot(x='Survived', y='Age', data=df)
ax5.set_title("Age vs Survival", fontsize=13)
ax5.set_xlabel("Survived")
ax5.set_ylabel("Age")

# 6️⃣ Correlation Heatmap
ax6 = plt.subplot(2,3,6)
correlation = df.corr(numeric_only=True)
sns.heatmap(
    correlation,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    square=True,
    cbar=True
)
ax6.set_title("Correlation Matrix", fontsize=13)

plt.suptitle(
    "Titanic Dataset – Exploratory Data Analysis Dashboard",
    fontsize=16,
    fontweight="bold"
)

plt.show()


# ==============================
# EXECUTIVE SUMMARY
# ==============================

print("\n==============================")
print("EXECUTIVE SUMMARY")
print("==============================")

print("""
1. Most passengers were between 20–40 years old.
2. Majority traveled in 3rd class.
3. Females had significantly higher survival rates.
4. First-class passengers had better survival chances.
5. Passenger class and gender influenced survival more than age.
""")

print("EDA Project Completed Successfully.")