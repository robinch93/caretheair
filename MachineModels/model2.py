#!C:\Users\Lenovo\AppData\Local\Programs\Python\Python37-32\python.exe

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import warnings
import pickle
from sklearn import model_selection
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
warnings.filterwarnings("ignore")

# read the data from excel or csv file and convert that data into numpy array.
data = pd.read_csv("InputFiles/vegetation.csv")
data = np.array(data)

# extracting x and y values from data sheet.
X = data[1:, 1:-1]    # in X, we have all independent features.(oxygen, temp, humidity)
Y = data[1:, -1]      # Y is for dependent feature (Fire occurrence)
# conerting them into integer values.
Y = Y.astype('int')
X = X.astype('int')
# print(X,y)
# splitting the data into test(30%) and training(70%)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=0)
model = LogisticRegression()  # calling the logistic regression model.

model.fit(X_train, Y_train)   # training the model by feeding the training set as input.

inputt=[int(x) for x in "45 32 60".split(' ')]
final=[np.array(inputt)]

b = model.predict_proba(final)
prediction = model.predict(X_test)

pickle.dump(model,open('model2.pkl','wb'))  # to create a pre compiled file
model=pickle.load(open('model2.pkl','rb'))

# cross validation
# cv = 10, means 10 diff. experiments will be done on X and Y.
results = model_selection.cross_val_score(model, X, Y, cv=10)

# confusion matrix
matrix = confusion_matrix(Y_test, prediction)
print(matrix)

# classification report
report = classification_report(Y_test, prediction)
print(report)

# accuracy score - this may differ based on changing random_state value in train_test_split method
acc_score = accuracy_score(prediction,Y_test)
print("accuracy score is: ", acc_score)

# Regression metrics
print("MAE: %.2f (%.2f)" % (results.mean(), results.std()))
