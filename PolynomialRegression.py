#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 21:12:41 2024
@author: Akram Khan
"""

# Polynomial Regression Demo
# --------------------------
# Polynomial regression is useful when the relationship between variables is nonlinear.
# This script demonstrates polynomial regression with examples of fitting data,
# evaluating the model using R-squared, and making predictions.

import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

# Example 1: Polynomial Regression on Realistic Data
# ---------------------------------------------------
# Data: Cars passing through a tollbooth
x = [1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 21, 22]
y = [100, 90, 80, 60, 60, 55, 60, 65, 70, 70, 75, 76, 78, 79, 90, 99, 99, 100]

# Create a polynomial regression model (degree 3)
model = np.poly1d(np.polyfit(x, y, 3))

# Generate line for plotting the polynomial curve
line = np.linspace(min(x), max(x), 100)

# Plotting the data and polynomial fit
plt.figure(figsize=(8, 5))
plt.scatter(x, y, color='blue', label='Data Points')
plt.plot(line, model(line), color='red', label='Polynomial Fit (Degree 3)')
plt.title('Polynomial Regression: Tollbooth Data')
plt.xlabel('X-axis (e.g., Time)')
plt.ylabel('Y-axis (e.g., Speed)')
plt.legend()
plt.grid(True)
plt.show()

# R-Squared Calculation
r_squared = r2_score(y, model(x))
print(f"R-squared value for the fit: {r_squared:.3f}")

# Example 2: Predicting Future Values
# ------------------------------------
# Predict the speed of a car passing at a specific point (e.g., x=17)
predicted_value = model(17)
print(f"Predicted speed at x=17: {predicted_value:.2f}")

# Example 3: Bad Fit Example
# ---------------------------
# Demonstrating a case where polynomial regression is not a good choice
x_bad = [89, 43, 36, 36, 95, 10, 66, 34, 38, 20, 26, 29, 48, 64, 6, 5, 36, 66, 72, 40]
y_bad = [21, 46, 3, 35, 67, 95, 53, 72, 58, 10, 26, 34, 90, 33, 38, 20, 56, 2, 47, 15]

# Create a polynomial regression model (degree 3)
model_bad = np.poly1d(np.polyfit(x_bad, y_bad, 3))

# Generate line for plotting
line_bad = np.linspace(min(x_bad), max(x_bad), 100)

# Plotting the data and polynomial fit
plt.figure(figsize=(8, 5))
plt.scatter(x_bad, y_bad, color='green', label='Data Points')
plt.plot(line_bad, model_bad(line_bad), color='orange', label='Polynomial Fit (Degree 3)')
plt.title('Bad Fit Example: Random Data')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid(True)
plt.show()

# R-Squared for Bad Fit
r_squared_bad = r2_score(y_bad, model_bad(x_bad))
print(f"R-squared value for the bad fit: {r_squared_bad:.3f}")
