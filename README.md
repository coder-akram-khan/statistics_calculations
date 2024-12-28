# statistics_calculations

This repository demonstrates Python code for calculating key statistical measures and performing basic data analysis. It also includes examples of **Linear Regression** to explore relationships between variables, make predictions, and highlight potential limitations.

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

---

## Visualizations

### Statistical Calculations
A box plot is used to visualize the data distribution:
- **Box Plot of Speed Data**
  ![Box Plot](https://github.com/coder-akram-khan/statistics_calculations/blob/main/stat.png?raw=true)

### Linear Regression
- **Linear Regression: Age vs Speed**
  ![Linear Regression Plot 1](https://github.com/coder-akram-khan/statistics_calculations/blob/main/linear_regression_plot1.png?raw=true)
- **Prediction for a 10-Year-Old Car**
  ![Linear Regression Plot 2](https://github.com/coder-akram-khan/statistics_calculations/blob/main/linear_regression_plot2.png?raw=true)
- **Bad Fit Example**
  ![Bad Fit Plot](https://github.com/coder-akram-khan/statistics_calculations/blob/main/linear_regression_bad_fit.png?raw=true)

---

## Usage

### Statistical Calculations
1. Install required libraries:
   ```bash
   pip install numpy matplotlib
   ```
2. Run the statistical script:
   ```bash
   python stat.py
   ```

### Linear Regression
1. Install required libraries:
   ```bash
   pip install matplotlib scipy
   ```
2. Run the regression script:
   ```bash
   python LinearRegression.py
   ```

The outputs will include predictions, R-values, and saved visualizations.

---

## Output

The script for statistical calculations will print:
- Mean
- Variance
- Standard Deviation
- Q1 (First Quartile)
- Q3 (Third Quartile)
- IQR (Interquartile Range)
- Lower Fence
- Upper Fence
- Outliers
- Deviations from the mean for each data point

The linear regression script will:
- Display scatter plots with fitted regression lines.
- Predict values for specific inputs.
- Highlight cases where linear regression is unsuitable (Bad Fit examples).

---

## Contributing

Contributions are welcome! Please feel free to fork this repository and submit pull requests with any improvements or enhancements.

---

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## About

This repository demonstrates Python code for calculating key statistical measures (mean, variance, standard deviation, quartiles, IQR) from a speed dataset. It also includes outlier detection using Tukey's method and a visual representation of the data distribution through a box plot. Linear Regression examples further illustrate basic machine learning concepts.
