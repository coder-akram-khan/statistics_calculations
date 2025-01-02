import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')


# Load dataset
df = pd.read_csv("cars.csv")

# Display dataset info
print("Dataset Shape:", df.shape)
print("Dataset Head:\n", df.head())
print("Dataset Columns:", df.columns)

# Independent and dependent variables
X = df[["Weight", "Volume"]]
y = df["CO2"]

# Create a linear regression model
regr = linear_model.LinearRegression()
regr.fit(X, y)

# Predict CO2 for a car with weight=2300kg and volume=1300
predictedCO2 = regr.predict([[2300, 1300]])
print(f"Predicted CO2 for Weight=2300kg and Volume=1300: {predictedCO2[0]:.2f}")

# Print coefficients
coefficients = regr.coef_
print(f"Coefficients: Weight={coefficients[0]:.6f}, Volume={coefficients[1]:.6f}")

# Predict CO2 for a car with weight increased by 1000kg (3300kg) and same volume
predictedCO2_increased_weight = regr.predict([[3300, 1300]])
print(f"Predicted CO2 for Weight=3300kg and Volume=1300: {predictedCO2_increased_weight[0]:.2f}")

# Manually verifying the calculation
manual_calculation = 107.2087328 + (1000 * coefficients[0])
print(f"Manually Verified CO2: {manual_calculation:.2f}")

# --- Visualization ---

# 1. Weight vs CO2
plt.figure(figsize=(8, 5))
plt.scatter(df["Weight"], y, color="blue", label="Actual CO2")
plt.plot(df["Weight"], regr.predict(X), color="red", label="Regression Line")
plt.xlabel("Weight (kg)")
plt.ylabel("CO2 Emission")
plt.title("Weight vs CO2 Emission")
plt.legend()
plt.savefig("weight_vs_co2.png")
plt.show()

# 2. Volume vs CO2
plt.figure(figsize=(8, 5))
plt.scatter(df["Volume"], y, color="green", label="Actual CO2")
plt.xlabel("Volume (cc)")
plt.ylabel("CO2 Emission")
plt.title("Volume vs CO2 Emission")
plt.legend()
plt.savefig("volume_vs_co2.png")
plt.show()

# 3. 3D Scatter Plot: Weight, Volume vs CO2
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df["Weight"], df["Volume"], y, color="purple", label="Actual CO2")
ax.set_xlabel("Weight (kg)")
ax.set_ylabel("Volume (cc)")
ax.set_zlabel("CO2 Emission")
ax.set_title("Weight & Volume vs CO2 Emission")
plt.legend()
plt.savefig("3d_weight_volume_vs_co2.png")
plt.show()
