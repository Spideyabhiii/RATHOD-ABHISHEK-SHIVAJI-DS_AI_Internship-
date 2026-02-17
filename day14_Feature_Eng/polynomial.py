import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score
#Create Non-Linear Data
np.random.seed(0)

X = np.linspace(-5, 5, 100).reshape(-1, 1)
y = 3 * X**2 + 2 * X + 1 + np.random.randn(100, 1) * 5

#Linear Regression (Original)
model_linear = LinearRegression()
model_linear.fit(X, y)
y_pred_linear = model_linear.predict(X)

r2_linear = r2_score(y, y_pred_linear)

print("R² Score (Linear Regression):", r2_linear)
#Polynomial Features (Degree 2)
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

model_poly = LinearRegression()
model_poly.fit(X_poly, y)
y_pred_poly = model_poly.predict(X_poly)
r2_poly = r2_score(y, y_pred_poly)

print("R² Score (Polynomial Regression):", r2_poly)

#Plot Comparison

plt.figure()
plt.scatter(X, y)
plt.plot(X, y_pred_linear)
plt.plot(X, y_pred_poly)
plt.title("Linear vs Polynomial Regression")
plt.show()
