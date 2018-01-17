import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import metrics

import PMLC.Ch04.utility as utility


data = utility.load_data('/Users/jasper/Desktop/HackerRank/PMLC/Ch04/data_perf.txt')
scores = []
range_values = np.arange(2, 10)

for i in range_values:
    kmeans = KMeans(init='k-means++',
                    n_clusters=i,
                    n_init=10)
    kmeans.fit(data)
    score = metrics.silhouette_score(data, kmeans.labels_,
                                     metric='euclidean',
                                     sample_size=len(data))
    print(score)
    scores.append(score)


plt.figure()
plt.bar(range_values, scores, width=0.6, color='k',
        align='center')
plt.title('Silhouette score vs number of clusters')

plt.figure()
plt.scatter(data[:, 0], data[:, 1], marker='o', color='k',
            facecolor='none', s=30)
x_min, x_max = min(data[:, 0]) - 1, max(data[:, 0]) + 1
y_min, y_max = min(data[:, 1]) - 1, max(data[:, 1]) + 1
plt.title('Input data')
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())
plt.show()