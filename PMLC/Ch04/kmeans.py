import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.cluster import KMeans

import PMLC.Ch04.utility as utility


data = utility.load_data('/Users/jasper/Desktop/HackerRank/PMLC/Ch04/data_multivar.txt')
num_cluster = 4

plt.figure()
plt.scatter(data[:, 0], data[:, 1], marker='o',
            facecolors='none', edgecolors='k', s=30)
plt.title('Input data')
x_min, x_max = min(data[:, 0]) - 1, max(data[:, 0] + 1)
y_min, y_max = min(data[:, 1]) - 1, max(data[:, 1] + 1)
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks()
plt.yticks()
plt.show()


kmeans = KMeans(init='k-means++', n_clusters=num_cluster, n_init=10)
kmeans.fit(data)

step_size = 0.01
x_min, x_max = min(data[:, 0]) - 1, max(data[:, 0]) + 1
y_min, y_max = min(data[:, 1]) - 1, max(data[:, 1]) + 1
x_values, y_values = np.meshgrid(np.arange(x_min, x_max, step_size),
                                 np.arange(y_min, y_max, step_size))
predict_labels = kmeans.predict(np.c_[x_values.ravel(),
                                      y_values.ravel()])

predict_labels = predict_labels.reshape(x_values.shape)
plt.figure()
plt.clf()
plt.imshow(predict_labels, interpolation='nearest',
           extent=(x_values.min(), x_values.max(), y_values.min(), y_values.max()),
           cmap=plt.cm.Paired, aspect='auto', origin='lower')
plt.scatter(data[:, 0], data[:, 1], marker='o', edgecolors='k', s=30)
centroids = kmeans.cluster_centers_
plt.scatter(centroids[:, 0], centroids[:, 1], marker='o', s=50, linewidths=3,
            color='k', zorder=10, facecolor='black')
plt.title('Centoids and boundaries obtained using kmeans')
x_min, x_max = min(data[:, 0]) - 1, max(data[:, 0] + 1)
y_min, y_max = min(data[:, 1]) - 1, max(data[:, 1] + 1)
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks()
plt.yticks()
plt.show()
