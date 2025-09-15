print("AMAAN SUHEAB")

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import root_mean_squared_error,r2_score


data=pd.read_csv("Advertising.csv")
print(data.head(5))
k=["Index","TV","Radio","Newspaper","Sales"]
data.columns=k
print(data.head(5))

print(data.isna().sum())

data=data.drop(columns=["Index"])

x=data.iloc[:,:3]
y=data["Sales"]
print(x,y)

print(data.describe())
print(data.shape)

tv = data['TV']
sales = data['Sales']

print(max(data["Sales"]),min(data["Sales"]))
plt.figure(figsize=(12, 6))
plt.bar(range(len(tv)), sales, color='skyblue', edgecolor='black', linewidth=1.2)


plt.xlabel("TV Advertising Spend Index", fontsize=12)
plt.ylabel("Sales (units sold)", fontsize=12)
plt.title("TV Advertising Spend vs Sales", fontsize=14)
plt.plot()
plt.show()


xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.25,random_state=100)
model=LinearRegression()
model.fit(xtrain,ytrain)

pred=model.predict(xtest)
print(ytest.shape)
print((pred.shape))
print(r2_score(pred,ytest))
print(root_mean_squared_error(pred,ytest))

