import sys
import numpy as np
from sklearn import linear_model
import matplotlib as plt

filename = sys.argv[1]
X = []
y = []
with open(filename, 'r') as f:
    for line in f.readlines():
        xt, yt = [float(i) for i in line.split(',')]
        X.append(xt)
        y.append(yt)

num_training = int(0.8 * len(X))
num_test = len(X) - num_training

X_train = np.array(X[:num_training]).reshape((num_training, 1))
y_train = np.array(y[:num_training])

X_test = np.array(X[num_training:]).reshape((num_test, 1))
y_test = np.array(y[num_training:])

linear_regressor = linear_model.LinearRegression()
linear_regressor.fit(X_train, y_train)

y_train_predict = linear_regressor.predict(X_train)


plt.figure()
plt.scatter(X_train, y_train, color='green')
plt.plot(X_train, y_train_predict, color='black', linewidth=4)
plt.title('Training data')
plt.show()

y_test_pred = linear_regressor.predict(X_test)
plt.scatter(X_test, y_test, color='green')
plt.plot(X_test, y_test_pred, color='black', linewidth=4)
plt.title('Test data')
plt.show()