# 📊 Unemployment Rate Prediction

This project aims to predict the **unemployment rate** based on various features such as **region**, **area**, **estimated employment**, and **labour participation rate**. The model used is a **Random Forest Regressor**, and the evaluation is done using **Root Mean Squared Error (RMSE)**, **Mean Absolute Error (MAE)**, and **R2 Score**.

---

## 👤 Author

**Amaan Suheab**

---

## 📊 Dataset

The dataset used is **unemp.csv**, which includes the following columns:

- **Region**: Geographical region.
- **Area**: Urban or rural classification.
- **Date**: Date of record.
- **Estimated Employed**: The number of employed people in thousands.
- **Estimated Labour Participation Rate (%)**: Percentage of the population participating in the workforce.
- **Estimated Unemployment Rate (%)**: Target variable — unemployment rate.

---

## 🧪 Process Overview

### 1. **Data Loading**
   - Load the `unemp.csv` file and inspect the structure.

### 2. **Data Preprocessing**
   - Clean and convert columns to numeric.
   - Handle missing values by dropping rows with missing target values.

### 3. **Feature Engineering**
   - Select relevant features for the model:
     - **Region**
     - **Area**
     - **Date**
     - **Estimated Employed**
     - **Estimated Labour Participation Rate (%)**

### 4. **Visualization**
   - Boxplot: **Rural vs Urban Unemployment Rate**.
   - Barplot: **Average Unemployment Rate by Region**.
   - Scatterplot: **Unemployment Rate vs Employed**.

### 5. **Model Training**
   - Train a **Random Forest Regressor** model.
   - Use a **Pipeline** with preprocessing and modeling steps.

### 6. **Evaluation**
   - Use **RMSE**, **MAE**, and **R2 Score** to evaluate the model.

---

## 🧾 Example Output

The following metrics were computed on the test data:


Test RMSE: 0.21
Test MAE: 0.16
Test R2: 0.98
📂 Project Structure
text
Copy code
unemployment-rate-prediction/
├── data/                      # Dataset folder (unemp.csv)
├── src/                       # Source code (model training, preprocessing)
│   └── model.py               # Main Python script
├── README.md                  # Project documentation
├── requirements.txt           # Python dependencies
├── .gitignore                 # Git ignore file
└── LICENSE                    # Project license
