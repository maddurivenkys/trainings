# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 17:32:00 2019

@author: e1012466
probability dense function
"""

import math as m

def normal_pdf(sigma=16, x,  mean=60):
    e= m.e
    pie=m.pi    
    A = (2*pie*(sigma**2))**0.5
    B = ((x-mean)**2/(2*sigma**2))    
    result = (mean.e**B)/A

    
    
 