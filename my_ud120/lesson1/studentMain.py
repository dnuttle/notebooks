#!/usr/bin/python

""" Complete the code in ClassifyNB.py with the sklearn
    Naive Bayes classifier to classify the terrain data.
    
    The objective of this exercise is to recreate the decision 
    boundary found in the lesson video, and make a plot that
    visually shows the decision boundary """


from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture, output_image
from ClassifyNB import classify


import numpy as np
import pylab as pl


features_train, labels_train, features_test, labels_test = makeTerrainData()

### the training data (features_train, labels_train) have both "fast" and "slow" points mixed
### in together--separate them so we can give them different colors in the scatterplot,
### and visually identify them
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]



# You will need to complete this function imported from the ClassifyNB script.
# Be sure to change to that code tab to complete this quiz.
clf = classify(features_train, labels_train)
accuracy = clf.score(features_test, labels_test)
print 'Accuracy: {0:.3f}'.format(accuracy)

from sklearn.svm import SVC
from sklearn.svm import LinearSVC


### draw the decision boundary with the text points overlaid
prettyPicture(clf, features_test, labels_test)
#output_image("test.png", "png", open("test.png", "rb").read())

for i in range(1,100, 20):
    c = float(i)/100.0
    c = float(i)
    for j in range(1,1000, 200):
        gamma = j
        clf = SVC(kernel='rbf', C=c, gamma=gamma)
        clf.fit(features_train, labels_train)
        print 'C: {0:.3f}, gamma: {1:d}, Accuracy: {2:.3f}'.format(c, gamma, clf.score(features_test, labels_test))

for i in range(1, 500, 50):
    clf = LinearSVC(C=i)
    clf.fit(features_train, labels_train)
    print 'C: {0:d}, Accuracy: {1:.3f}'.format(i, clf.score(features_test, labels_test))
