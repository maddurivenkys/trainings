# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 21:35:32 2019

@author: e1012466
"""

l=[10,10,11,11,11,11,12,12,12,12,13,13,14,14,15]
#please find the mode

unique = set(l);

print(unique)
d={}
for i in unique:
    d[i] = 0

print(d)

for i in l:
    d[i]=d[i]+1

mode=0
largest_count=0
for key, value in d.items():
    if largest_count<value:
        largest_count=value
        mode=key
print(mode)
