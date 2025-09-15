
print('AMAAN SUHEAB')

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,precision_score
from sklearn.metrics import confusion_matrix,classification_report
import matplotlib.pyplot as plt
data = pd.read_csv("spam.csv", encoding='ISO-8859-1', header=None, usecols=[0, 1])
data.columns = ['label', 'message']
print(data.head())

print(data['label'].value_counts())

le = LabelEncoder()
data['label'] = le.fit_transform(data['label'])
print(data.head(5))

 
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(data['message'])

print(X)
print(data.head(6))

Y=data['label']

xtrain,xtest,ytrain,ytest=train_test_split(X,Y,test_size=0.25,random_state=100)

model = LogisticRegression(max_iter=1000)
model.fit(xtrain, ytrain)


ypred = model.predict(xtest)

print("Accuracy:", accuracy_score(ytest, ypred)*100)
print("\nConfusion Matrix:\n", confusion_matrix(ytest, ypred))
print("\nClassification Report:\n", classification_report(ytest, ypred))

