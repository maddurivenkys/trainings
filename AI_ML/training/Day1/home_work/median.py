# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 21:55:07 2019

@author: e1012466
"""

# is a floor division operator which will round the result to nearest integer

# Python program to print 
# median of elements 

# list of elements to calculate median 
n_num = [1, 2,7, 8, 9,3, 4, 5,6]
n = len(n_num) 
n_num.sort() 

if n % 2 == 0: 
	median1 = n_num[n//2] 
	median2 = n_num[n//2 - 1] 
	median = (median1 + median2)/2
else: 
	median = n_num[n//2] 
print("Median is: " + str(median)) 
