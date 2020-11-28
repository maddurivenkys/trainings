# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 13:55:33 2019

@author: e1012466
"""

# function definition
def mean(x):
    """This is function calculates mean of a list; input: List type object of int or float type; 
    it will return a float"""
    s=0
    count=0
    for i in x:
        s=s+i
        count=count+1
    m=s/count
    return m

# function for variance
def variance(x):
    var=0;
    m=mean(x)
    c=len(x)
    for Xi in x:
        var=var+(Xi-m)**2
        var=var/c;
    return var;

# function for Standar devication
def standard_deviation(x):    
    return variance(x)**0.5