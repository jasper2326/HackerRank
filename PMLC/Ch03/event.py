import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.svm import SVC
from sklearn import model_selection


input_file = '/Users/jasper/Desktop/HackerRank/PMLC/Ch03/building_event_binary.txt'

X = []
count = 0
with open(input_file, 'r') as f:
    for line in f.readlines():
        data = line.split(',')
        X.append([data[0]] + data[2:])
X = np.array(X)


label_encoder = []
X_encoded = np.empty(X.shape)
for i, item in enumerate(X[0]):
    if item.isdigit():
        X_encoded[:, i] = X[:, i]
    else:
        label_encoder.append(preprocessing.LabelEncoder())
        X_encoded[:, i] = label_encoder[-1].fit_transform(X[:, 1])


X = X_encoded[:, :-1].astype(int)
y = X_encoded[:, -1].astype(int)


params = {'kernel': 'rbf', 'probability': True, 'class_weight': 'balanced'}
classifier = SVC(**params)
classifier.fit(X, y)


accuracy = model_selection.cross_val_score(classifier,
                                           X, y, scoring='accuracy',
                                           cv=3)
print(round(accuracy.mean(), 2))


# input_data = ['Tuesday', '12:30:00', '21', '23']
# input_data_encoded = [-1] * len(input_data)
# count = 0
# for i, item in enumerate(input_data):
#     if item.isdigit():
#         input_data_encoded[i] = int(item)
#     else:
#         input_data_encoded[i] = int(label_encoder[count].inverse_transform(item))
#         count = count + 1
#
#input_data_encoded = np.array(input_data_encoded)

# Predict and print output for a particular datapoint
output_class = classifier.predict(input_data_encoded)
print("Output class:", label_encoder[-1].inverse_transform(output_class)[0])