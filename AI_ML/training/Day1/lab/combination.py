# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 15:16:44 2019

@author: e1012466

nCr = n! / r! * (n - r)!
"""

def factorial (x):
    if x==1 or x==0:
        return 1
    else:
        return x*factorial(x-1)
print('factorial ', factorial(4));


def combination(n,x):
    return factorial(n)/(factorial(x) * factorial(n-x))

print('combination ', combination(6,0))

#print(combination(6,0)*(0.3**0)*(0.7**6))


# binominal function
def binomial(x, n, p):
    return combination(n,x)*(p**x)*((1-p)**(n-x))

print('binomial ', binomial(6, 6, 0.3))


# probability of all 6 bullets
  # print( binomial(6, 6, 0.3));

# find probaility of atleast 3 bullets
print( binomial(6,6,0.3)+ binomial(5,6,0.3)+ binomial(4,6,0.3)+binomial(3,6,0.3));

# ONG 
# sciencetist oil = 10% of chance of oil 
# they have identified 10 

print('ONGC binomial ', binomial((0, 10, 0.1)));
      
print('students coming to class',binomial(18,16,0.9)+ binomial(18,17,0.9)+ binomial(18,18,0.9));


def cumulative_binomial(x, n, p):
    total=0
    for i in range(0, x+1):
        total=total+binomial(1,n,p)
    return total

print(1-cumulative_binomial(15,18,0.9))