import numpy as np
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.svm import SVC
from sklearn.metrics import classification_report
import PMLC.Ch03.svm.


input_file = '/Users/jasper/Desktop/HackerRank/PMLC/Ch03/data_multivar_imbalance.txt'
X, y = load_data()