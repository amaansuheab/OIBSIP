print("AMAAN SUHEAB")



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from datetime import datetime

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score


data = pd.read_csv("unemp.csv")


data.columns = [i.strip() for i in data.columns]


print(data.head(5))
print(data.isna().sum())
print(data.columns)
print(data.describe())
print(data.shape)

target = "Estimated Unemployment Rate (%)"


data[target] = pd.to_numeric(data[target], errors='coerce')
data["Estimated Employed"] = pd.to_numeric(data["Estimated Employed"], errors='coerce')
data["Estimated Labour Participation Rate (%)"] = pd.to_numeric(data["Estimated Labour Participation Rate (%)"], errors='coerce')


print("Missing rows before drop:\n", data.isnull().sum())


data = data.dropna(subset=[target])

print("After Dropping Rows\n", data.isnull().sum())

plt.figure(figsize=(10, 5))
data.groupby("Date")[target].mean().plot()
plt.xticks(rotation=90)
plt.ylabel("Unemployment Rate (%)")
plt.title("Average Unemployment Rate over Time")
plt.tight_layout()
plt.show()


features = ["Region", "Area", "Date",
            "Estimated Employed", "Estimated Labour Participation Rate (%)"]

X = data[features]
y = data[target]


categorical = ["Region", "Area", "Date"]
numeric = ["Estimated Employed", "Estimated Labour Participation Rate (%)"]

preprocessor = ColumnTransformer([
    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical),
    ("num", StandardScaler(), numeric)
])

pipeline = Pipeline([
    ("pre", preprocessor),
    ("model", RandomForestRegressor(n_estimators=200, random_state=0))
])

plt.figure(figsize=(8,5))
sns.boxplot(x="Area", y=target, data=data)
plt.title("Rural vs Urban Unemployment Rate")

plt.show()

plt.figure(figsize=(12,6))
sns.barplot(x="Region", y=target, data=data, estimator=np.mean, ci=None)
plt.xticks(rotation=90)
plt.title("Average Unemployment Rate by Region")

plt.show()

plt.figure(figsize=(8,5))
sns.scatterplot(x="Estimated Employed", y=target, hue="Area", data=data, alpha=0.7)
plt.title("Unemployment Rate vs Employed")

plt.show()


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

pipeline.fit(X_train, y_train)
preds = pipeline.predict(X_test)

rmse = np.sqrt(mean_squared_error(y_test, preds))
mae = mean_absolute_error(y_test, preds)
r2 = r2_score(y_test, preds)

print("Test RMSE:", rmse)
print("Test MAE :", mae)
print("Test R2  :", r2)
