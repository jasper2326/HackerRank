from itertools import cycle

import numpy as np
from sklearn.cluster import DBSCAN
from sklearn import metrics
import matplotlib.pyplot as plt

import PMLC.Ch04.utility as utility


data = utility.load_data('/Users/jasper/Desktop/HackerRank/PMLC/Ch04/data_perf.txt')
eps_grid = np.linspace(0.3, 1.2, num=10)
silhouette_scores = []
silhouette_score_max = -1
eps_best = eps_grid[0]
best_model = None
labels_best = None

for eps in eps_grid:
    model = DBSCAN(eps=eps).fit(data)
    labels = model.labels_
    silhouette_score = metrics.silhouette_score(data, labels)
    silhouette_scores.append(silhouette_score)
    print(round(eps, 2), '-->', round(silhouette_score, 4))

    if silhouette_score > silhouette_score_max:
        silhouette_score_max = silhouette_score
        eps_best = eps
        best_model = model
        labels_best = labels


plt.figure()
plt.bar(eps_grid, silhouette_scores, width=0.05, color='k', align='center')
plt.title('Silhouette score vs epsilon')
plt.show()


print(eps_best)
offset = 0
if -1 in labels_best:
    offset = 1

num_cluster = len(set(labels_best)) - offset
print(num_cluster)

mask_core = np.zeros(labels_best.shape, np.bool)
mask_core[best_model.core_sample_indices_] = True


plt.figure()
labels_unique = set(labels_best)
markers = cycle('vo^s<>')
for cur_label, marker in zip(labels_unique, markers):
    if cur_label == -1:
        marker = '.'
    cur_mask = labels_best == cur_label

    cur_data = data[cur_mask & mask_core]
    plt.scatter(cur_data[:, 0], cur_data[:, 1], marker=marker,
                edgecolors='black', s=96, facecolors='none')

    cur_data = data[cur_mask & ~mask_core]
    plt.scatter(cur_data[:, 0], cur_data[:, 1], marker=marker,
                edgecolors='black', s=32)

plt.title('Data separated into clusters')
plt.show()