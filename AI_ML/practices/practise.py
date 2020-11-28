# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 22:12:14 2019

@author: e1012466
"""

import pandas as pd
import numpy as np

df = pd.DataFrame({'AAA' : [4,5,6,7], 'BBB': [10,20,30,40], 
                   'CCC': [100,50, -30, -50]});

print(df)

df.loc[df.AAA >=5, 'BBB'] ==-1; 
print(df)

df['logic']= np.where(df['AAA'] > 5, 'high', 'low')
print(df)

newseries = df.loc[(df['BBB'] < 25) & (df['CCC'] >= -40), 'AAA']; 
print(newseries)

data = {'AAA' : [4,5,6,7], 'BBB' : [10,20,30,40],'CCC' : [100,50,-30,-50]}
df2 = pd.DataFrame(data=data,index=[1,2,3,4]); #

df2.iloc[1:3] #Position-oriented
print(df)
