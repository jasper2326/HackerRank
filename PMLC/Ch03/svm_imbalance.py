import numpy as np
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.svm import SVC
from sklearn.metrics import classification_report
import PMLC.Ch03.svm as svm


input_file = '/Users/jasper/Desktop/HackerRank/PMLC/Ch03/data_multivar_imbalance.txt'
X, y = svm.load_data(input_file)

class_0 = np.array([X[i] for i in range(len(X)) if y[i] == 0])
class_1 = np.array([X[i] for i in range(len(X)) if y[i] == 1])

plt.figure()
plt.scatter(class_0[:, 0], class_0[:, 1],
            facecolors='black', edgecolors='black',
            marker='s')
plt.scatter(class_1[:, 0], class_1[:, 1],
            facecolors='None', edgecolors='black',
            marker='s')
plt.title('Input Data')
plt.show()


X_train, X_test, y_train, y_test = \
    model_selection.train_test_split(X, y, test_size=0.25, random_state=5)
params = {'kernel': 'linear',
          'class_weight': 'balanced'}
classifier = SVC(**params)
classifier.fit(X_train, y_train)

svm.plot_classifier(classifier, X_train, y_train, 'Training dataset')
plt.show()


target_names = ['Class-' + str(int(i)) for i in set(y)]
print('\n' + '#' * 30)
print(classification_report(y_train, classifier.predict(X_train),
                            target_names=target_names))
print('\n' + '#' * 30)
print(classification_report(y_test, classifier.predict(X_test),
                            target_names=target_names))