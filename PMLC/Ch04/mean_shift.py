import numpy as np
from sklearn.cluster import MeanShift, estimate_bandwidth
import matplotlib.pyplot as plt
from itertools import cycle

import PMLC.Ch04.utility as utility


X = utility.load_data('/Users/jasper/Desktop/HackerRank/PMLC/Ch04/data_multivar.txt')
bandwidth = estimate_bandwidth(X, quantile=0.1)
meanshift_estimator = MeanShift(bandwidth, bin_seeding=True)

meanshift_estimator.fit(X)
labels = meanshift_estimator.labels_
centroids = meanshift_estimator.cluster_centers_
num_clusters = len(np.unique(labels))
print(num_clusters)


plt.figure()
markers = '.*xv'
for i, marker in zip(range(num_clusters), markers):
    plt.scatter(X[labels==i, 0], X[labels==i, 1], marker=marker,
                color='k')
    centroid = centroids[i]
    plt.plot(centroid[0], centroid[1], marker='o',
             markerfacecolor='k', markeredgecolor='k', markersize=15)
plt.title('Clusters and their centroids')
plt.show()