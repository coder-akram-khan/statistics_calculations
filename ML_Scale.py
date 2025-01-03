# Scaling Script with Saveable Plots
import pandas as pd
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("cars.csv")

# Original data
x = df[['Weight', "Volume"]]
y = df['CO2']

# Before scaling: Weight vs Volume
plt.figure(figsize=(8, 6))
plt.scatter(df['Weight'], df['Volume'], color='blue', alpha=0.6)
plt.title("Before Scaling: Weight vs Volume")
plt.xlabel("Weight")
plt.ylabel("Volume")
plt.grid(True)
plt.savefig("before_scaling_weight_vs_volume.png")
plt.close()

# Scale data
scale = StandardScaler()
scaled_x = scale.fit_transform(x)

# After scaling: Weight vs Volume
plt.figure(figsize=(8, 6))
plt.scatter(scaled_x[:, 0], scaled_x[:, 1], color='green', alpha=0.6)
plt.title("After Scaling: Weight vs Volume")
plt.xlabel("Scaled Weight")
plt.ylabel("Scaled Volume")
plt.grid(True)
plt.savefig("after_scaling_weight_vs_volume.png")
plt.close()

# Train regression model
regr = linear_model.LinearRegression()
regr.fit(scaled_x, y)

# Prediction using scaled data
scaled_input = scale.transform([[2300, 1.3]])
predictedCO2 = regr.predict([scaled_input[0]])
print(f"Predicted CO2 Emission for scaled input: {predictedCO2[0]}")

# Save prediction plot
plt.figure(figsize=(8, 6))
plt.bar(["Original"], [predictedCO2[0]], color='orange', alpha=0.7)
plt.title("Predicted CO2 Emission after Scaling")
plt.ylabel("CO2 Emission")
plt.savefig("predicted_co2_after_scaling.png")
plt.close()
