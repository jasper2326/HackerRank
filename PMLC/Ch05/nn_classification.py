import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from sklearn import neighbors, datasets

from PMLC.Ch05.utility import load_data


input_file = '/Users/jasper/Desktop/HackerRank/PMLC/Ch05/data_nn_classifier.txt'
data = load_data(input_file)
X, y = data[:, :-1], data[:, -1].astype(np.int)

plt.figure()
plt.title('Input datapoints')
markers = '^sov<>hp'
mapper = np.array([markers[i] for i in y])
print(mapper)


for i in range(X.shape[0]):
    plt.scatter(X[i, 0], X[i, 1], marker=mapper[i], s=50,
                edgecolors='black', facecolors='none')
plt.show()


num_neighbors = 10
h = 0.01
classifier = neighbors.KNeighborsClassifier(n_neighbors=num_neighbors,
                                            weights='distance')
classifier.fit(X, y)

x_min, x_max = data[:, 0].min() - 1, data[:, 0].max() + 1
y_min, y_max = data[:, 1].min() - 1, data[:, 1].max() + 1
x_grid, y_grid = np.meshgrid(np.arange(x_min, x_max, h),
                             np.arange(y_min, y_max, h))


predicted_values = classifier.predict(np.c_[x_grid.ravel(),
                                          y_grid.ravel()])
predicted_values = predicted_values.reshape(x_grid.shape)


plt.figure()
plt.pcolormesh(x_grid, y_grid, predicted_values, cmap=cm.Pastel1)
for i in range(X.shape[0]):
    plt.scatter(X[i, 0], X[i, 1], marker=mapper[i], s=50,
                edgecolors='black', facecolors='none')
plt.xlim(x_grid.min(), x_grid.max())
plt.ylim(y_grid.min(), y_grid.max())
plt.title('k nearest neighbors classifier boundaries')


test_datapoint = [4.5, 3.6]
plt.figure()
plt.title('Test datapoint')
for i in range(X.shape[0]):
    plt.scatter(X[i, 0], X[i, 1], s=50, marker=mapper[i],
                edgecolors='black', facecolor='none')

plt.scatter(test_datapoint[0], test_datapoint[1], s=200,
            marker='x', facecolor='black', linewidths=3)


dist, indices = classifier.kneighbors([test_datapoint])
plt.figure()
plt.title('k nearest neighbors')
for i in indices:
    plt.scatter(X[i, 0], X[i, 1], marker='o', linewidths=3,
                s=100, facecolor='black')
plt.scatter(test_datapoint[0], test_datapoint[1], marker='x', s=500,
            edgecolors='black', facecolor='black')

for i in range(X.shape[0]):
    plt.scatter(X[i, 0], X[i, 1], s=50, marker=mapper[i],
                edgecolors='black', facecolor='none')
plt.show()