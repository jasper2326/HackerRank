import csv

import numpy as np
from sklearn import cluster, covariance, manifold
from sklearn.cluster import MeanShift, estimate_bandwidth
import matplotlib.pyplot as plt


input_file = '/Users/jasper/Desktop/HackerRank/PMLC/Ch04/wholesale.csv'
file_reader = csv.reader(open(input_file, 'r'), delimiter=',')
X = []
for count, row in enumerate(file_reader):
    if not count:
        names = row[2:]
        continue
    X.append([float(x) for x in row[2:]])

X = np.array(X)

bandwidth = estimate_bandwidth(X, quantile=0.8, n_samples=len(X))
meanshift_estimator = MeanShift(bandwidth=bandwidth, bin_seeding=True)
meanshift_estimator.fit(X)
labels = meanshift_estimator.labels_
centroids = meanshift_estimator.cluster_centers_
num_cluster = len(np.unique(labels))
print(num_cluster)


print('\nCentroids of clusters:')
print('\t'.join([name[:3] for name in names]))
for centroid in centroids:
    print('\t'.join([str(int(x)) for x in centroid]))


centroids_milk_groceries = centroids[:, 1:3]
plt.figure()
plt.scatter(centroids_milk_groceries[:, 0], centroids_milk_groceries[:, 1],
            s=10, edgecolor='k', facecolor='none')
offset = 0.2
plt.xlim(centroids_milk_groceries[:, 0].min() - offset * centroids_milk_groceries[:, 0].ptp(),
         centroids_milk_groceries[:, 0].max() + offset * centroids_milk_groceries[:, 0].ptp(),)
plt.ylim(centroids_milk_groceries[:, 1].min() - offset * centroids_milk_groceries[:, 1].ptp(),
         centroids_milk_groceries[:, 1].max() + offset * centroids_milk_groceries[:, 1].ptp())

plt.title('Centroids of clusters for milk and groceries')
plt.show()