from sklearn.linear_model import SGDRegressor
from sklearn.datasets import load_diabetes, load_breast_cancer, fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, log_loss, mean_squared_error
import numpy as np
import time
import sys


X,y = load_diabetes(return_X_y=True)

y = y / y.max()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.25, random_state=0)



start_time = time.time()

#scaler = StandardScaler()
#X_train = scaler.fit_transform(X_train)
#X_test = scaler.fit_transform(X_test)

def train_sgd_model(X_train,y_train, epochs,batch_size):

	num_samples = X_train.shape[0]
	num_batches = num_samples // batch_size
	
	sgd = SGDRegressor(random_state=0)
	
	
	for epoch in range(epochs):
		for batch in range(num_batches):
			start_index = batch * batch_size
			end_index = start_index + batch_size
			X_batch = X_train[start_index:end_index]
			y_batch = y_train[start_index:end_index]
			sgd.partial_fit(X_batch, y_batch)	
	return sgd

sgd = train_sgd_model(X_train,y_train, 10,32)
#sgd.fit(X_train,y_train)

y_pred = sgd.predict(X_test)

accuracy = mean_squared_error(y_test,y_pred)

print("Mean squared error", accuracy)

print("Total time:", (time.time() - start_time))
