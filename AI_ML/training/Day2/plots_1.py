# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 13:52:39 2019

@author: e1012466
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline
import seaborn as sns


# read xcels
res= pd.read_csv("file:///C://Users//e1012466//chennai-water-management//chennai_reservoir_levels.csv")
rain= pd.read_csv("file:///C://Users//e1012466//chennai-water-management//chennai_reservoir_rainfall.csv")


rain.Date=pd.to_datetime(rain.Date, format="%d-%m-%Y)
rain.index=rain.Date


plt.scatter(rain.CHEMBARAMBAKKAM, res.CHEMBARAMBAKKAM)

def covariance(x,y):
    cov=0
    xmu=np.mean(x)
    ymu=np.mean(y)
    for i in range(len(x)):
        cov=cov+(x[i]-xmu)*(y[i]-ymu)
        cov=cov/len(x)
    return cov

def pearsonR(x,y):
    cov=covariance(x,y)
    pr=cov/(np.std(x)*np.std(y))
    return pr

res["Year"]=res.Date.map(lambda x: x.year)
rain["Year"]=res.Date.map(lambda x: x.year)

res.groupby("Year")["CHEMBARAMBAKKAM].mean()


plt.scatter(rain_chem, res_chem)
print(pearsonR(rain))

from scipy.stats import pearsonr
plt.scatter(rain_chem, res_chem.shift(-1))

res_chem.shift(-1).dropna() # to drop null values


print(covariance(res.CHEMBARAMBAKKAM.values, rain.CHEMBARAMBAKKAM.values))



#Y: Res Level
#X: Rainfall
#Y= mx+c


X=pd.DataFrame(data("Rainfall":rain_chem))

X["Bias"]=1

X=X.values
Y=res_chem.values

def least_sq_method(X,Y):
    B=np.dot(np.li.inv(np.dot(X, T, X)),np.dot(X, T, Y))
    return B

least_sq_method(X,Y)

def predit

