# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 15:16:37 2019

@author: e1012466
"""


# HW - mean absolute error

def mse(y, y_hat):
    error=0
    for i in range(0, len(y)):
        error=error+(y[i]-y_hat[1])
    return error

mse(Y,y_hat)


def  rmse(y, y_hat):
    return mse(y, y_hat)**0.5

rmse(Y, y_hat) # root mean square root error


# Residual Analysis used to know error 

