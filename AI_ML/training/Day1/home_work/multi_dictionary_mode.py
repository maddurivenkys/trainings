# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 06:50:10 2019

@author: e1012466
"""
def mode(l):
    #1:use set to find unique elements
    s=set(l)
#2: Create a null dict and store all unique elements with count values as 0
    d={}
    for i in s:
        d[i]=0
#3: count the occurance and update the counts
    for i in l:
        d[i]=d[i]+1
#4: find the key of lagest value in dict 
    mode=[]
    largest_count=0
    for key, value in d.items():
        if largest_count<value:
            largest_count=value
            mode=key
        #elif largest_count == value:
        #    mode.append(key)
            
        
    #Homework: for multimodal dist; update the logic
    return mode

#print(dic)
def multimode(dic):
    
    for key, value in dic.items():
        print (key, value)     
        if(type(value) is dict):
            print("type of value is a dictionary") 
            multimode(value)
        elif(type(value) is list):
            print("type value is not a dictionary")
            mode1= mode(value)
            print("Mode of ", key , " is ", mode1)
        else:
            print("type(value)", type(value) , "is not supported ")

l=[10,10,11,11,11,11,12,12,12,12,13,13,14,14,15]
l1=[20,20,21,21,21,21,22,22,22,22,23,23,24,24,25]
l2=[30,30,31,31,31,31,32,32,32,32,33,33,34,34,35]
#please find the mode

dic = {"v1":l, "v2": l1}

dic1 = {"v3": l2}

#print('dic1', type(dic1))

dic["v3"]=dic1

#print(type(dic))

multimode(dic)            
        
      

