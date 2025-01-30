#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 23:29:25 2025

@author: akram
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics

# -----------------------------
# Confusion Matrix Explanation
# -----------------------------
# - Rows represent actual classes
# - Columns represent predicted classes
# - Helps to analyze model performance

# Generate synthetic classification data
np.random.seed(42)
actual = np.random.binomial(1, 0.9, size=1000)   # Actual labels
predicted = np.random.binomial(1, 0.9, size=1000) # Predicted labels

# Compute Confusion Matrix
conf_matrix = metrics.confusion_matrix(actual, predicted)

# Display Confusion Matrix
cm_display = metrics.ConfusionMatrixDisplay(conf_matrix, display_labels=["Negative", "Positive"])
cm_display.plot(cmap="Blues", values_format="d")
plt.title("Confusion Matrix")
plt.savefig("plots_figs/confusion_matrix.png")
plt.show()

# -----------------------------
# Classification Metrics
# -----------------------------
accuracy = metrics.accuracy_score(actual, predicted)
precision = metrics.precision_score(actual, predicted)
recall = metrics.recall_score(actual, predicted)
specificity = metrics.recall_score(actual, predicted, pos_label=0)
f1score = metrics.f1_score(actual, predicted)

# Print Evaluation Metrics
print(f"Accuracy: {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall (Sensitivity): {recall:.4f}")
print(f"Specificity: {specificity:.4f}")
print(f"F1-Score: {f1score:.4f}")

# -----------------------------
# Precision-Recall Curve
# -----------------------------
precision_values, recall_values, _ = metrics.precision_recall_curve(actual, predicted)

plt.figure(figsize=(6, 4))
plt.plot(recall_values, precision_values, marker='.', color='red', label="Precision-Recall Curve")
plt.xlabel("Recall (Sensitivity)")
plt.ylabel("Precision")
plt.title("Precision-Recall Curve")
plt.legend()
plt.grid()
plt.savefig("plots_figs/precision_recall_curve.png")
plt.show()
