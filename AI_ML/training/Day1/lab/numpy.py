# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 14:02:46 2019

@author: e1012466
"""

import numpy as np

a=np.array([1,2,3,4,5,6])
print(a)

b=np.ndarray
print(b)

print('mean ', a.mean())

# dimension of array
print(' dimension ', a.ndim);

print('dtype ', a.dtype);
#dtype('int32')

#np.array([1.1, 32, 45, 65]), dtype=str)
#b=b.astype(float)


#generate some random numbers

x=np.arange(1, 21)
print(' randmon numbers ', x)
y=x.reshape(5, 4)
print(' matrix ', y);

print('random rows and columsn ', y[0:2])

print(y[0:3,1:3])

"""
np.save("m_matrix", m)
n= np.load(m_matrix.npy")

np.savetxt('m_matrix.txt',n)

a>5

a[m>10]

a[m*10]

# matrix multiplication 
# 2*3 3*2


#a.T # matrix transpose

#a.linalg.inv 
"""