# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 12:22:36 2019

@author: e1012466

use case : chennai water magangement 
"""

import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline
import seaborn as sns


# read xcels
res= pd.read_csv("file:///C://Users//e1012466//chennai-water-management//chennai_reservoir_levels.csv")
rain= pd.read_csv("file:///C://Users//e1012466//chennai-water-management//chennai_reservoir_rainfall.csv")

plt.plot(res.POONDI)
plt.show

res.index= res.Date
plt.figure(figsize=(20,4))
plt.plot(res.POONDI, label="POONDI")
plt.plot(res.CHOLAVARAM, label="CHOLAVARAM")
plt.plot(res.REDHILLS, label="REDHILLS")
plt.plot(res.CHEMBARAMBAKKAM, label="CHEMBARAMBAKKAM")
plt.legend()
plt.show()

print('stats', res.POONDI.describe())

plt.hist(res.POONDI)
plt.show
plt.hist(res.REDHILLS)
plt.show


res["Month"]=res.Date.map(lambda x: x.month)

grouped_res = res.groupby("Month").mean()

sns.barplot(X="index", y="POONDI", data=grouped_res)

sns.distplot(res.POONDI)
sns.distplot(res.REDHILLS)



