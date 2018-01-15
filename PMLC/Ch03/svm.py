import numpy as np
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.svm import SVC
from sklearn.metrics import classification_report


def load_data(input_file):
    X = []
    y = []
    with open(input_file, 'r') as f:
        for line in f.readlines():
            data = [float(x) for x in line.split(',')]
            X.append(data[:-1])
            y.append(data[-1])

    X = np.array(X)
    y = np.array(y)
    return X, y


input_file = '/Users/jasper/Desktop/HackerRank/PMLC/Ch03/data_multivar.txt'
X, y = load_data(input_file)

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
params = {'kernel': 'rbf'}
classifier = SVC(**params)
classifier.fit(X_train, y_train)


def plot_classifier(classifier, X, y, title='Classifier boundaries',
                    annotate=False):
    x_min, x_max = min(X[:, 0]) - 1.0, max(X[:, 0] + 1.0)
    y_min, y_max = min(X[:, 1]) - 1.0, max(X[:, 1] + 1.0)
    step_size = 0.01

    x_values, y_values = np.meshgrid(np.arange(x_min, x_max, step_size),
                                     np.arange(y_min, y_max, step_size))
    mesh_output = classifier.predict(np.c_[x_values.ravel(),
                                           y_values.ravel()])
    mesh_output = mesh_output.reshape(x_values.shape)


    plt.figure()
    plt.title(title)
    plt.pcolormesh(x_values, y_values, mesh_output, cmap=plt.cm.gray)
    plt.scatter(X[:, 0], X[:, 1], c=y, s=80, edgecolors='black',
                linewidths=1, cmap=plt.cm.Paired)

    plt.xlim(x_values.min(), x_values.max())
    plt.ylim(y_values.min(), y_values.max())
    plt.xticks()
    plt.yticks()

    if annotate:
        for x, y in zip(X[:, 0], X[:, 1]):
            # Full documentation of the function available here:
            # http://matplotlib.org/api/text_api.html#matplotlib.text.Annotation
            plt.annotate(
                '(' + str(round(x, 1)) + ',' + str(round(y, 1)) + ')',
                xy = (x, y), xytext = (-15, 15),
                textcoords = 'offset points',
                horizontalalignment = 'right',
                verticalalignment = 'bottom',
                bbox = dict(boxstyle = 'round,pad=0.6', fc = 'white', alpha = 0.8),
                arrowprops = dict(arrowstyle = '-', connectionstyle = 'arc3,rad=0'))


plot_classifier(classifier, X_train, y_train, 'Training dataset')
plt.show()


target_names = ['Class-' + str(int(i)) for i in set(y)]
print('\n' + '#' * 30)
print(classification_report(y_train, classifier.predict(X_train),
                            target_names=target_names))
print('\n' + '#' * 30)
print(classification_report(y_test, classifier.predict(X_test),
                            target_names=target_names))