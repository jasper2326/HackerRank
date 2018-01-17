import json
import datetime

import numpy as np
import matplotlib.pyplot as plt
from sklearn import covariance, cluster
from mpl_finance import quotes_historical_yahoo_ochl as quotes_yahoo


symbol_file = '/Users/jasper/Desktop/HackerRank/PMLC/Ch04/symbol_map.json'
start_date = datetime.datetime(2004, 4, 5)
end_date = datetime.datetime(2007, 6, 2)

with open(symbol_file, 'r') as f:
    symbol_dict = json.loads(f.read())

symbols, names = np.array(list(symbol_dict.items())).T

quotes = [quotes_yahoo(symbol, start_date, end_date, asobject=True) for symbol in symbols]

opening_quotes = np.array([quote.open for quote in quotes]).astype(np.float)
closing_quotes = np.array([quote.close for quote in quotes]).astype(np.float)

# The daily fluctuations of the quotes
delta_quotes = closing_quotes - opening_quotes

# Build a graph model from the correlations
edge_model = covariance.GraphLassoCV()

# Standardize the data
X = delta_quotes.copy().T
X /= X.std(axis=0)

# Train the model
with np.errstate(invalid='ignore'):
    edge_model.fit(X)

# Build clustering model using affinity propagation
_, labels = cluster.affinity_propagation(edge_model.covariance_)
num_labels = labels.max()

# Print the results of clustering
for i in range(num_labels + 1):
    print("Cluster", i+1, "-->", ', '.join(names[labels == i]))