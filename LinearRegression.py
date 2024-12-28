#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 18:03:43 2024

@author: akram
"""

import matplotlib.pyplot as plt
from scipy import stats

# Example 1: Basic Linear Regression
# -----------------------------------
x_age = [5, 7, 8, 7, 2, 17, 2, 9, 4, 12, 12, 9, 6]
y_speed = [77, 86, 87, 22, 86, 103, 87, 37, 94, 78, 77, 85, 86]

# Perform linear regression
slope, intercept, r, p, std_error = stats.linregress(x_age, y_speed)

def predict(x):
    return slope * x + intercept

# Model predictions
model = list(map(predict, x_age))

# Visualization
plt.figure(figsize=(8, 5))
plt.scatter(x_age, y_speed, color='blue', label='Data Points')
plt.plot(x_age, model, color='red', label=f'Linear Fit\nR={r:.2f}')
plt.title('Linear Regression: Age vs Speed')
plt.xlabel('Age of Car (years)')
plt.ylabel('Speed (km/h)')
plt.legend()
plt.grid(True)
plt.savefig('linear_regression_plot1.png')
plt.show()

# Example 2: Predicting Future Values
# ------------------------------------
x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
y = [99, 86, 89, 63, 103, 18, 99, 37, 94, 78, 77, 85, 86]

# Perform linear regression
slope, intercept, r, p, std_error = stats.linregress(x, y)

# Prediction for a 10-year-old car
predicted_speed = predict(10)
print(f"Predicted speed for a 10-year-old car: {predicted_speed:.2f} km/h")

# Visualization
model = list(map(predict, x))
plt.figure(figsize=(8, 5))
plt.scatter(x, y, color='green', label='Data Points')
plt.plot(x, model, color='orange', label=f'Linear Fit\nR={r:.2f}')
plt.scatter(10, predicted_speed, color='red', label=f'Prediction (10 years)\nSpeed={predicted_speed:.2f}')
plt.title('Linear Regression: Predicting Speed')
plt.xlabel('Age of Car (years)')
plt.ylabel('Speed (km/h)')
plt.legend()
plt.grid(True)
plt.savefig('linear_regression_plot2.png')
plt.show()

# Example 3: Bad Fit Example
# ---------------------------
x_bad = [89, 43, 36, 36, 95, 34, 56, 45, 78, 90, 23, 56, 56,
         78, 90, 45, 67, 90, 58, 10]
y_bad = [45, 56, 9, 46, 90, 78, 3, 12, 10, 21, 4, 89, 78, 16,
         45, 8, 30, 10, 4, 78]

# Perform linear regression
slope, intercept, r, p, std_error = stats.linregress(x_bad, y_bad)

def bad_fit_predict(x):
    return slope * x + intercept

# Visualization
model_bad = list(map(bad_fit_predict, x_bad))
plt.figure(figsize=(8, 5))
plt.scatter(x_bad, y_bad, color='purple', label='Data Points')
plt.plot(x_bad, model_bad, color='brown', label=f'Linear Fit\nR={r:.2f}')
plt.title('Bad Fit Example: Random Data')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid(True)
plt.savefig('linear_regression_bad_fit.png')
plt.show()

# Summary
# --------
print("Key Points:")
print("1. R value close to 1 or -1 indicates strong linear relationship.")
print("2. R value close to 0 indicates weak or no linear relationship.")
print("3. Bad fit examples show when linear regression is not suitable.")































