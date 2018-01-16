import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm, model_selection
from sklearn.metrics import classification_report

import PMLC.Ch03.svm as svm


input_file = '/Users/jasper/Desktop/HackerRank/PMLC/Ch03/data_multivar.txt'
X, y = svm.load_data(input_file)


X_train, X_test, y_train, y_test = \
    model_selection.train_test_split(X, y, test_size=0.25,
                                     random_state=5)

parameter_grid = [{'kernel': ['linear'], 'C': [1, 10, 50, 600]},
                  {'kernel': ['poly'], 'degree': [2, 3]},
                  {'kernel': ['rbf'], 'gamma': [0.01, 0.001], 'C': [1, 10, 50, 600]}]

metrics = ['precision', 'recall_weighted']
for metric in metrics:
    classifier = model_selection.GridSearchCV(svm.SVC(C=1),
                                              parameter_grid,
                                              cv=5,
                                              scoring=metric)
    classifier.fit(X_train, y_train)

    for params, avg_score, _ in classifier.grid_scores_:
        print(params, '-->', round(avg_score, 3))

    y_true, y_pred = y_test, classifier.predict(X_test)
    print(classification_report(y_true, y_pred))