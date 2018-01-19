import numpy as np
import matplotlib.pyplot as plt
from sklearn import neighbors


amplitude = 10
num_points = 100
X = amplitude * np.random.rand(num_points, 1) - 0.5 * amplitude

y = np.sinc(X).ravel()
y += 0.2 * (0.5 - np.random.rand(y.size))


plt.figure()
plt.scatter(X, y, s=50, edgecolors='black', facecolors='blue')
plt.title('Input data')

x_values = np.linspace(-0.5 * amplitude,
                       0.5 * amplitude,
                       10 * num_points)[:, np.newaxis]
n_neighbors = 8


knn_regressor = neighbors.KNeighborsRegressor(n_neighbors,
                                              weights='distance')
knn_regressor.fit(X, y)
y_values = knn_regressor.predict(x_values)

plt.figure()
plt.scatter(X, y, s=20, c='red', facecolors='none', label='input data')
plt.plot(x_values, y_values, c='blue', linestyle='--',
         label='predicted values')
plt.xlim(X.min() - 1, X.max() + 1)
plt.ylim(y.min() - 0.2, y.max() + 0.2)
plt.axis('tight')
plt.legend()
plt.title('K Nearest Neighbors Regressor')

plt.show()
