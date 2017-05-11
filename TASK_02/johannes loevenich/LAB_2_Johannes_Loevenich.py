# -*- coding: utf-8 -*-
"""
Created on Thu May 11 10:52:22 2017

@author: JohannesLoevenich
"""

import nltk
from nltk.corpus import stopwords
import collections, re
from nltk.corpus import wordnet as wn

# BoW Histogram
def printwords(abc):
    words = [ collections.Counter(re.findall(r'\w+', txt))
            for txt in removedStopwords]
    sumOfBags = sum(words, collections.Counter())
    print(sumOfBags)
    return

# Return senses of word
def WordnetSenses(word):
    print(wn.synsets(word))
    return

def UpdateStops(word):
    stops.update((word))
    

#Extract the original set of words
stops = set(stopwords.words("english"))
file =  open("Input.txt","r")
Input = file.readline()
word_token = nltk.word_tokenize(Input)
#add additional stop words
# word = 'only'
#stops.update(word)
#Check to remove stop words
removedStopwords = [w for w in word_token if not w in stops]
print(word_token)
print(removedStopwords)
printwords(removedStopwords)
#WordnetSenses('Berlin')