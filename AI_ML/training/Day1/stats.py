# function defintion
def mean(x):
    """This function calculates mean of a list; input: List type object of
    int or float type; it will return a float"""
    s=0
    count=0
    for i in x:
        s=s+i
        count=count+1
    mu=s/count
    return mu

def variance(x):
    mu=mean(x)
    var=0
    for Xi in x:
        var=var+(Xi-mu)**2
    var=var/count
    return var
def standard_deviation(x):
    return variance(x)**0.5

l=[10,10,11,11,11,11,12,12,12,12,13,13,14,14,15]
#please find the mode

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
    mode=0
    largest_count=0
    for key, value in d.items():
        if largest_count<value:
            largest_count=value
            mode=key
    #Homework: for multimodal dist; update the logic
    return mode