# -*- coding: utf-8 -*-

from sklearn import svm
from featurevec import *
import datetime


X = [[0, 0], [0, 0], [1, 1], [2, 2], [3, 3]]
Y = [0, 0, 1, 2, 3]
# clf = svm.SVC()
clf = svm.LinearSVC()
clf.fit(X, Y) 
out = clf.predict([[1, 1], [0, 0], [2, 0]])
print out.tolist()