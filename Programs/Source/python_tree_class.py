from sklearn.linear_model import SGDRegressor
from sklearn.datasets import load_diabetes, load_breast_cancer, fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, log_loss, mean_squared_error
from sklearn.tree import DecisionTreeClassifier
import numpy as np
import time
import sys


X,y = load_breast_cancer(return_X_y=True)

#y = y / y.max()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.25, random_state=0)


start_time = time.time()

tree = DecisionTreeClassifier(max_depth=5)

tree.fit(X_train,y_train)

y_pred = tree.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)

print("Total time:", (time.time() - start_time))

