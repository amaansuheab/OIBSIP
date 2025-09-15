# 📊 Advertising Sales Prediction

This project uses machine learning techniques to predict **Sales** based on advertising expenditure across three media channels: **TV**, **Radio**, and **Newspaper**.

---

## 👤 Author

**Amaan Suheab**

---

## 📁 Dataset

The dataset `Advertising.csv` contains the following columns:

- `TV`: TV advertising budget in thousands of dollars
- `Radio`: Radio advertising budget in thousands of dollars
- `Newspaper`: Newspaper advertising budget in thousands of dollars
- `Sales`: Sales generated (in units)
- `Index`: Index number (dropped in preprocessing)

---

## 🔬 Project Objective

To train regression models to predict **Sales** using **Linear Regression** and analyze the effectiveness of advertising channels.

---

## 🧪 Process Overview

### 1. Data Loading
- Load `Advertising.csv`.
- Rename and clean columns.

### 2. Preprocessing
- Drop unnecessary `Index` column.
- Split dataset into features (`TV`, `Radio`, `Newspaper`) and target (`Sales`).

### 3. Visualization
- Plot **TV ad spend vs Sales** to see direct relationship.

### 4. Model Training
- Train a **Linear Regression** model.
- Split data using `train_test_split`.

### 5. Evaluation
- Use **R² Score** and **Root Mean Squared Error (RMSE)** for performance evaluation.

---

## 🧾 Sample Code Output


R2 Score: 0.93
RMSE: 1.54
📂 Project Structure

```
Advertising-Sales-Prediction/
├── data/
│   └── Advertising.csv
├── src/
│   └── advertising_model.py
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE
```
