# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 09:59:33 2019

@author: e1012466

Problem:

Suppose that accidents occur in a factory at a rate of 1/20 per working day. Suppose in the factory six days
are working and we begin observing het occurrence of accidents at the starting of work on Monday. Let X be the number of
days unitl the fisrst accidents occurs. Find the probability that first week is accident free.


"""
import math as m
from scipy.integrate import quad

def exponDistribution(x, lam=1/20):
    return lam*(m.e**(-lam*x))

prob, error = quad(exp_pdf, a=0, b=6)
p = 1-prob

print (' exponDistribution ', p)