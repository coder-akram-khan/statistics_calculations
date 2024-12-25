#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 16:08:02 2024

@author: akram
"""

#statistics_calculations
import numpy as np
import matplotlib.pyplot as plt

def calculate_statistics(data):
    """
    Calculate various statistical measures for a sample dataset, including:
      - Mean
      - Variance
      - Standard Deviation
      - Lower Fence
      - Upper Fence
      - Outliers (based on Tukey's method)
      - Deviations from the mean

    Args:
      data: A list of numerical values.

    Returns:
      A dictionary containing the calculated statistics.
    """

    mean = np.mean(data)
    deviations = [x - mean for x in data]
    squared_deviations = [d**2 for d in deviations]
    variance = np.mean(squared_deviations)
    std_dev = np.sqrt(variance)

    # Calculating quartiles
    q1, q3 = np.percentile(data, [25, 75])
    iqr = q3 - q1

    # Calculating Tukey's fences
    lower_fence = q1 - (1.5 * iqr)
    upper_fence = q3 + (1.5 * iqr)

    # Identify outliers
    outliers = [x for x in data if x < lower_fence or x > upper_fence]

    return {
        "mean": mean,
        "variance": variance,
        "std_dev": std_dev,
        "deviations": deviations,
        "q1": q1,
        "q3": q3,
        "iqr": iqr,
        "lower_fence": lower_fence,
        "upper_fence": upper_fence,
        "outliers": outliers
    }

# Sample data
speed = [32, 111, 138, 28, 59, 77, 97]

#  statistics
stats = calculate_statistics(speed)

# boxplot
plt.boxplot(speed)
plt.title("Speed Data Distribution")
plt.ylabel("Speed")
plt.show()

# Print results in a table
print("Speed Data Analysis")
print("-" * 30)
print(f"Mean:\t\t\t{stats['mean']:.2f}")
print(f"Variance:\t\t\t{stats['variance']:.2f}")
print(f"Standard Deviation:\t\t{stats['std_dev']:.2f}")
print(f"Q1:\t\t\t{stats['q1']:.2f}")
print(f"Q3:\t\t\t{stats['q3']:.2f}")
print(f"IQR:\t\t\t{stats['iqr']:.2f}")
print(f"Lower Fence:\t\t{stats['lower_fence']:.2f}")
print(f"Upper Fence:\t\t{stats['upper_fence']:.2f}")
print(f"Outliers:\t\t{stats['outliers']}")
print("\nDeviations from Mean:")
for i, deviation in enumerate(stats["deviations"]):
    print(f"Data Point {i+1}:\t{deviation:.2f}")


















































