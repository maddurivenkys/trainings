# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 23:37:59 2020

@author: e1012466
"""

import nltk

text='Mary had a little lamb. Her fleece was white as snow'
from nltk.tokenize import word_tokenize, sent_tokenize
sents=sent_tokenize(text)
print(sents)