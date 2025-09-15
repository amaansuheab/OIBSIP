# 🌸 Iris Flower Classification

This project uses machine learning to classify the **Iris flower** species based on features such as **sepal length**, **sepal width**, **petal length**, and **petal width**. The model used is **Logistic Regression**, and performance is evaluated using accuracy, precision, recall, and confusion matrix.

---

## 👤 Author

**Amaan Suheab**

---

## 📊 Dataset

The **Iris dataset** contains 150 samples of iris flowers, each described by the following features:

- **Sepal Length (cm)**
- **Sepal Width (cm)**
- **Petal Length (cm)**
- **Petal Width (cm)**

The target variable is the **species** of the flower, which can be one of the following classes:
- **Setosa**
- **Versicolor**
- **Virginica**

---

## 🧪 Process Overview

### 1. **Data Loading**
   - Load the `iris.csv` dataset and inspect the structure.

### 2. **Data Preprocessing**
   - Drop the **Id** column (not needed for classification).
   - Check for missing values and inspect the general data distribution.

### 3. **Model Training**
   - Split the dataset into training and testing sets using **train_test_split**.
   - Train a **Logistic Regression** model on the training data.

### 4. **Evaluation**
   - Evaluate the model using **Accuracy**, **Precision**, **Classification Report**, and **Confusion Matrix**.

---

## 📈 Example Output

The following evaluation metrics were calculated on the test data:


Accuracy: 98.67%
Precision Score: 97.0%
Classification Report:
              precision    recall  f1-score   support
           Setosa       98.0      100.0      99.0        38
       Versicolor       100.0      97.4       98.7        38
        Virginica       98.1      97.4       97.7        38
    accuracy                           98.7       114
   macro avg       98.4      98.3       98.3       114
weighted avg       98.4      98.7       98.6       114

📂 Project Structure

iris-flower-classification/
├── data/                      # Dataset folder (iris.csv)
├── src/                       # Source code (model training, prediction)
│   └── model.py               # Main Python script
├── README.md                  # Project documentation
├── requirements.txt           # Python dependencies
├── .gitignore                 # Git ignore file
└── LICENSE                    # Project license
