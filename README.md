# Statistics and Machine Learning

This repository demonstrates Python code for calculating key statistical measures and performing basic data analysis. It also includes examples of **Linear Regression**, **Polynomial Regression**, and **Multiple Regression** to explore relationships between variables, make predictions, and highlight potential limitations.

![ml](https://github.com/coder-akram-khan/statistics_calculations/blob/main/ml.jpg?raw=true")

---

## Key Features

### 1. Statistical Calculations

- Calculates key statistical measures such as:
  - Mean
  - Variance
  - Standard Deviation
  - Quartiles (Q1, Q3) and Interquartile Range (IQR)
- Detects outliers using Tukey's method.
- Visualizes data distribution with a box plot.

### 2. Linear Regression Demonstrations

- **Basic Regression**: Shows the relationship between `Age of Car` and `Speed` using a linear regression model.
- **Prediction Example**: Predicts the speed of a car given its age (e.g., 10 years).
- **Bad Fit Example**: Demonstrates cases where linear regression is not suitable, using random data.
- Saved visualizations:
  - `linear_regression_plot1.png`: Age vs Speed relationship.
  - `linear_regression_plot2.png`: Prediction for a 10-year-old car.
  - `linear_regression_bad_fit.png`: Example of a poor linear regression fit.

### 3. Polynomial Regression Demonstrations (New)

- **Polynomial Regression**: Explores fitting data using polynomial regression models, evaluating them with R-squared, and making predictions.
- **Example 1: Realistic Data**: Demonstrates polynomial regression on car tollbooth data.
- **Example 2: Prediction**: Predicts the speed of a car at a specific point using the fitted model.
- **Example 3: Bad Fit**: Showcases a scenario where polynomial regression is not suitable (random data).
### 4. Multiple Regression (New)

- **Multiple Regression**: Uses more than one independent variable to predict a dependent variable.
- **CO2 Emission Example**: Predicts CO2 emissions of cars based on their `Weight` and `Volume`.
- **Coefficient Analysis**: Explains the relationship between independent variables and the predicted value.
- **Scenarios**:
  - Predicts CO2 emissions for a car with a weight of 2300 kg and volume of 1300 cc.
  - Demonstrates the impact of increasing weight by 1000 kg on CO2 emissions.
- Saved visualizations:
  - `multiple_regression_prediction.png`: Visualization of predicted CO2 for sample inputs.
  - `multiple_regression_coefficients.png`: Coefficient analysis plot.
### 5. Scaling and Standardization (New)

- Demonstrates the importance of scaling features when working with data of different units and ranges.
- Uses StandardScaler to standardize Weight and Volume columns from the `cars.csv` dataset.
- Includes a prediction of CO2 emissions for a car with specified features after scaling.


---

## Visualizations

### Statistical Calculations

A box plot is used to visualize the data distribution:- **Box Plot of Speed Data**
  ![Box Plot](https://github.com/coder-akram-khan/statistics_calculations/blob/main/stat.png?raw=true)

### Linear Regression

**Linear Regression: Age vs Speed**

![Linear Regression Plot 1](https://github.com/coder-akram-khan/statistics_calculations/blob/main/linear_regression_plot1.png?raw=true)

**Prediction for a 10-Year-Old Car**

![Linear Regression Plot 2](https://github.com/coder-akram-khan/statistics_calculations/blob/main/linear_regression_plot2.png?raw=true)

**Bad Fit Example**

![Bad Fit Plot](https://github.com/coder-akram-khan/statistics_calculations/blob/main/linear_regression_bad_fit.png?raw=true)

### Polynomial Regression 

**Polynomial Regression: Tollbooth Data**

![Polynomial Regression Plot 1](https://github.com/coder-akram-khan/statistics_calculations/blob/main/goodfipolynomial.png?raw=true)

**Prediction for x=17**


**Bad Fit Example: Random Data**

![Bad Fit Plot](https://github.com/coder-akram-khan/statistics_calculations/blob/main/badfitpolynomial.png?raw=true)

### Multiple Regression 
**CO2 Emission Prediction: Weight vs CO2**  
![Weight vs CO2](https://github.com/coder-akram-khan/statistics_calculations/blob/main/volume_vs_co2.png?raw=true)

**CO2 Emission Prediction: Volume vs CO2**  
![Volume vs CO2](https://github.com/coder-akram-khan/statistics_calculations/blob/main/volume_vs_co2.png?raw=true)

### Combined Analysis

**3D Visualization: Weight, Volume, and CO2 Emissions**  
![3D Weight, Volume vs CO2](https://github.com/coder-akram-khan/statistics_calculations/blob/main/3d_weight_volume_vs_co2.png?raw=true)

### ML Scaling (New)

**Before Scaling: Weight vs Volume**
   ![Before Scaling](https://github.com/coder-akram-khan/statistics_calculations/blob/main/before_scaling_weight_vs_volume.png?raw=true)

**After Scaling: Weight vs Volume**
   ![After Scaling](https://github.com/coder-akram-khan/statistics_calculations/blob/main/after_scaling_weight_vs_volume.png?raw=true)

**Predicted CO2 Emission after Scaling**
   ![Predicted CO2](https://github.com/coder-akram-khan/statistics_calculations/blob/main/predicted_co2_after_scaling.png?raw=true)
       
---
## Usage

1. Clone this repository:  
   ```bash
   git clone https://github.com/coder-akram-khan/statistics_calculations.git
   cd statistics_calculations
2. Install required libraries:  
   ```bash
   pip install -r requirements.txt
3. Run individual scripts for demonstrations:  
   ```bash
    python stat.py
    python LinearRegression.py
    python PolynomialRegression.py
    python multipleregression.py
   python ML_Scale.py
