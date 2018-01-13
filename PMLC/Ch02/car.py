import numpy as np
from sklearn import preprocessing
from sklearn import model_selection
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt


input_file = 'car.data.txt'

# Reading the data
X = []
y = []
count = 0
with open(input_file, 'r') as f:
    for line in f.readlines():
        data = line[:-1].split(',')
        X.append(data)

X = np.array(X)

# Convert string data to numerical data
label_encoder = []
X_encoded = np.empty(X.shape)
for i,item in enumerate(X[0]):
    label_encoder.append(preprocessing.LabelEncoder())
    X_encoded[:, i] = label_encoder[-1].fit_transform(X[:, i])

X = X_encoded[:, :-1].astype(int)
y = X_encoded[:, -1].astype(int)

# Build a Random Forest classifier
params = {'n_estimators': 200,
          'max_depth': 8,
          'random_state': 7}
classifier = RandomForestClassifier(**params)
classifier.fit(X, y)


accuracy = model_selection.cross_val_score(classifier,
                                           X, y, scoring='accuracy',
                                           cv=3)
print(round(accuracy.mean(), 2))


input_data = ['vhigh', '2', 'small', 'low']
input_data_encoded = [-1] * len(input_data)

