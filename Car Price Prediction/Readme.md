# 🚗 Car Price Prediction

This project uses machine learning to predict car prices based on various features such as car brand, mileage, fuel type, engine capacity, and more. The goal is to build a regression model that can accurately predict the price of a car based on the provided features.

---

## 👤 Author

**Amaan Suheab**

---

## 📦 Libraries Used

- `pandas` for data manipulation
- `numpy` for numerical computations
- `matplotlib` and `seaborn` for data visualization
- `scikit-learn` for machine learning and evaluation

---

## 📊 Dataset

The dataset used in this project is **car prices**, which includes the following features:

- **Make**: The brand or manufacturer of the car.
- **Model**: The model of the car.
- **Year**: Year of manufacture.
- **Mileage (km)**: The total distance the car has traveled.
- **Fuel Type**: Type of fuel used (e.g., petrol, diesel, electric).
- **Engine Capacity (L)**: Engine size in liters.
- **Transmission**: Type of transmission (e.g., automatic, manual).
- **Price**: The target variable — the price of the car.

### Data source: (Include if external source or link here)

---

## 🧪 Process Overview

### 1. **Data Loading**
   - Load the dataset and inspect the structure.

### 2. **Data Preprocessing**
   - Clean the dataset by removing irrelevant columns or handling missing values.
   - Convert categorical variables to numeric (e.g., using OneHotEncoding).
   - Standardize or normalize numerical features where needed.

### 3. **Feature Engineering**
   - Select relevant features for the model.
   - Split the dataset into features (`X`) and target (`y`).

### 4. **Visualization**
   - Various plots to explore the data:
     - **Distribution of car prices** to understand the target variable.
     - **Correlation heatmap** to explore relationships between features.
     - **Scatter plots** for price vs. mileage, engine capacity, etc.

### 5. **Model Training**
   - We use **Random Forest Regressor** to predict car prices.

### 6. **Evaluation Metrics**
   - **RMSE (Root Mean Squared Error)** for error measurement.
   - **MAE (Mean Absolute Error)** for understanding average prediction error.
   - **R2 Score** to assess model fit.

---


---

## 📁 File Structure

```
car-price-prediction/
├── Data/                      # Dataset folder (car_prices.csv)
├── src/                       # Source code (data preprocessing, model training, etc.)
├── .gitignore                 # Git ignore file
├── LICENSE                    # Project license
├── README.md                  # Project documentation
└── requirements.txt           # Python dependencies
```
