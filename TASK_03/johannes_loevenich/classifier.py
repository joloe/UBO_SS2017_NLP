# -*- coding: utf-8 -*-
"""
Created on Wed May 17 13:09:29 2017

@author: JohannesLoevenich
"""


import nltk
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import numpy as np
from sklearn.model_selection import train_test_split


# This is how the Naive Bayes classifier expects the input
def create_word_features(words):
    useful_words = [word for word in words if word not in stopwords.words("english")]
    my_dict = dict([(word, True) for word in useful_words])
    return my_dict

#get the positive reviews
reviews = []
file =  open("positive.txt","r")
pos_tokens = [word_tokenize(comment) for comment in file]
for token in pos_tokens:
    token =[ word.lower() for word in token if word.isalpha()]
    token = [w for w in token if not w in stopwords.words("english")]
    token = dict([(word, True) for word in token])
    reviews.append((token,"pos"))
#print(len(pos_reviews))

#get the negative reviews
file_neg =  open("negative.txt","r")
neg_tokens = [word_tokenize(comment_neg) for comment_neg in file_neg]
for token in neg_tokens:
    token =[ word.lower() for word in token if word.isalpha()]
    token = [w for w in token if not w in stopwords.words("english")]
    token = dict([(word, True) for word in token])
    reviews.append((token,"neg"))
#print(len(neg_reviews))

#define test and training set 85% training 15% test
print(len(reviews))
X_train, X_test, y_train, y_test = train_test_split(reviews,reviews, test_size=0.8, random_state=1234)
#print(X_train)
train_set = X_train 
test_set = X_test 
#define bayse classifier 
classifier = NaiveBayesClassifier.train(train_set)

#print the accuracy
accuracy = nltk.classify.util.accuracy(classifier, test_set)

#create a result file 
rfile = open('result.txt', 'w')
for comment in test_set:
    token = comment[0]
    rfile.write(str(token) + "     " + classifier.classify(token) + "\n")

print(accuracy * 100)
rfile.close()
file.close()
#Input = file.readline()
#word_token = nltk._(Input)