#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn.svm import SVC
#clf = SVC(kernel="linear")
clf = SVC(kernel="rbf", C=10000.)

# features_train=features_train[:len(features_train)/100]
# labels_train=labels_train[:len(labels_train)/100]

t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

t0 = time()
pred = clf.predict(features_test)
count = 0
for i in pred.flat:
    if i == 1: count +=1
print count
print "predicting time:", round(time()-t0, 3), "s"
# print clf.predict(features_test[10])
# print clf.predict(features_test[26])
# print clf.predict(features_test[50])

from sklearn.metrics import accuracy_score
accuracy = accuracy_score(pred, labels_test)
print accuracy
#########################################################

