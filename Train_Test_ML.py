#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 18:55:05 2025
@author: akram
"""

# Train-Test Split in Machine Learning:
# Train-test splitting helps evaluate how well a model generalizes to unseen data.

import numpy as np
from matplotlib import pyplot as plt
from sklearn.metrics import r2_score

# Step 1: Generate Synthetic Dataset
np.random.seed(2)
x = np.random.normal(3, 1, 100)
y = np.random.normal(140, 50, 100) / x

# Visualize the data
plt.scatter(x, y, color='blue')
plt.title("Customer Behavior: Minutes vs Spending")
plt.xlabel("Minutes Before Purchase")
plt.ylabel("Money Spent (USD)")
plt.savefig('plots_figs/behaviour_plot.png')
plt.show()

# Step 2: Train-Test Split (80% Training, 20% Testing)
train_x = x[:80]
train_y = y[:80]
test_x = x[80:]
test_y = y[80:]

# Visualize Training Data
plt.scatter(train_x, train_y, color='red', label='Training Data')
plt.title("Training Data")
plt.xlabel("Minutes Before Purchase")
plt.ylabel("Money Spent (USD)")
plt.legend()
plt.savefig('plots_figs/train_behaviour_plot.png')
plt.show()

# Visualize Testing Data
plt.scatter(test_x, test_y, color='green', label='Testing Data')
plt.title("Testing Data")
plt.xlabel("Minutes Before Purchase")
plt.ylabel("Money Spent (USD)")
plt.legend()
plt.savefig('plots_figs/test_behaviour_plot.png')
plt.show()

# Step 3: Polynomial Regression
mymodel = np.poly1d(np.polyfit(train_x, train_y, 4))
myline = np.linspace(0, 6, 100)

# Visualize Regression Fit
plt.scatter(train_x, train_y, color='red', label='Training Data')
plt.plot(myline, mymodel(myline), color='blue', label='Polynomial Fit')
plt.title("Polynomial Regression Fit")
plt.xlabel("Minutes Before Purchase")
plt.ylabel("Money Spent (USD)")
plt.legend()
plt.savefig('plots_figs/train_behaviour_regression_plot.png')
plt.show()

# Step 4: Evaluate Model with R-squared
train_r2 = r2_score(train_y, mymodel(train_x))
test_r2 = r2_score(test_y, mymodel(test_x))
print(f"R-squared for Training Data: {train_r2:.2f}")
print(f"R-squared for Testing Data: {test_r2:.2f}")

# Step 5: Predict Spending for 5 Minutes in Shop
minutes = 5
predicted_spending = mymodel(minutes)
print(f"Predicted Spending for {minutes} minutes: ${predicted_spending:.2f}")
