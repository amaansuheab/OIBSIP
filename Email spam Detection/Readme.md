# 📧 Spam Email Classification

This project aims to classify email messages as **spam** or **non-spam** using machine learning techniques. The **Logistic Regression** model is used in combination with text vectorization to classify messages. We use a dataset of labeled emails and process the text using **CountVectorizer** to extract meaningful features.

---

## 👤 Author

**Amaan Suheab**

---

## 📦 Libraries Used

- `pandas` for data manipulation
- `scikit-learn` for machine learning (Logistic Regression, Label Encoding, Count Vectorization)
- `matplotlib` for data visualization
- `ISO-8859-1` for reading special characters in the dataset

---

## 📊 Dataset

The dataset used in this project is **spam.csv**, which contains the following columns:

- **label**: Indicates if the message is **spam** or **ham** (non-spam).
- **message**: The text content of the email message.

### Data Source: (Link or mention where the data is sourced from)

---

## 🧪 Process Overview

### 1. **Data Loading**
   - Load the `spam.csv` file and inspect the structure.

### 2. **Data Preprocessing**
   - Clean and process the data:
     - Convert labels to numerical values (using **LabelEncoder**).
     - Vectorize the text data (using **CountVectorizer**).

### 3. **Model Training**
   - **Logistic Regression** is used to train the classification model on the features derived from the email messages.

### 4. **Model Evaluation**
   - Evaluate the model using **Accuracy**, **Confusion Matrix**, and **Classification Report**.

---

## 📈 Example Output

The following evaluation metrics were calculated on the test data:

Accuracy: 97.5%
Confusion Matrix:
[[1215 30]
[ 25 875]]

Classification Report:
precision recall f1-score support
0 0.98 0.98 0.98 1245
1 0.97 0.97 0.97 900
accuracy 0.98 2145
macro avg 0.98 0.98 0.98 2145
weighted avg 0.98 0.98 0.98 2145




---

## 📁 File Structure

```
spam-classification/
├── data/                      # Dataset folder (spam.csv)
├── src/                       # Source code (model training, preprocessing)
├── .gitignore                 # Git ignore file
├── LICENSE                    # Project license
├── README.md                  # Project documentation
└── requirements.txt           # Python dependencies

```
