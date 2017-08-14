# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 16:39:10 2017

@author: Home
"""

import numpy as np
from itertools import groupby

def nan_helper(lst):
    nans=[]
    for i, item in enumerate(lst): 
        if isinstance(item, (int, float, complex, bool)) == False:
           nans.append(i) 
    return(nans)
#def nextNum(lst):
#    for item in lst:    
#        if isinstance(item, (int, float, complex, bool)) == False:
from itertools import groupby
from operator import itemgetter                
from itertools import starmap
def cind(nind):
    data = [ 1, 4,5,6, 10, 15,16,17,18, 22, 25,26,27,28]
    for k, g in groupby(enumerate(data), lambda x : x[0] + x[1]):
        print(map(itemgetter(1), g))  
   

            

data = [ 1, 4,5,6, 10, 15,16,17,18, 22, 25,26,27,28]
#for k, g in groupby(enumerate(data), lambda i, x: i-x):
#    print map(itemgetter(1), g)                        
    
def consectInds(lst):
    pos = (j - i for i, j in enumerate(nan_helper(lst)))
    t = 0
    for i, els in groupby(pos):
        l = len(list(els))
        el = lst[t]
        t += l
        yield range(el, el+l)
        
        
y= np.array([23, 25, 28, None, None, 32, 30, 'dzfghas', 23])
nani = nan_helper(y)








    
def nextnan(lst):
    inds=[]
    for index, item in enumerate(lst):    
        
        if isinstance(item, (int, float, complex, bool)) == False:
            
            inds.append(index)
    return(inds)            
               
        #else: nestrepl(item,what, repl)

myarray=['Hello', 'how', 'how', ['are', 'what', 'how'], 'you', 'how']

myarray    
    
def intetype():
    return(-1)


def nestreplM(lst, what, repl):
    for index, item in enumerate(lst):
        if type(item) == list:
            nestreplM(item, what, repl)
        else:
            if item == what:
                lst[index] = repl

def nanchk(lst):
    #if len(lst) == 1: return(lst)
    ls=lst[1:]
    inds=[]
    target=(int, float, complex, bool)    
    for index, item in enumerate(lst):
        if index == len(lst) - 1: break
        if isinstance(lst[index], (target)) == False:
            print('\n current item index %s val false %s' % (index, lst[index]))
            #catches prev nan        
            #catches post nan
            if isinstance(lst[index + 1], (target)) == True:
                inds.append([index, lst[index + 1]])
                print('\n next item index %s val true %s' % (index + 1, lst[index + 1]) )
            
            else: 
                if isinstance(lst[index - 1], (target)) == True:
                    inds.append([index, (lst[index])])
                    print(' \n previous item index %s val true %s' % (index, lst[index]))
        
def nanchk2(lst,target=(int, float, complex, bool)):
    
    indvals=[]
    res=[]
    j=-1
    for i in range(0,len(lst)):
            
        if isinstance(lst[i], (target)) == False:
            if isinstance(lst[i-1], target) == True:
                indvals.append([[i, lst[i-1]]])
                #j+=1
            elif isinstance(lst[i+1], target) == True:
                    indvals[j].append([i+1,lst[i+1]])
                    #print(' i-1 %s i %s i+1 %s' % (lst[i-1], lst[i], lst[i+1]))
                    
#                    for k in range(0, len(indvals)):
#                        start=(i,indvals[k][0][1] )
#                        end=(i, indvals[k][1][1]) 
#                        lngth=indvals[k][1][0] - indvals[k][0][0] +2
                        
           
            
    
    return(indvals)
chkpress=nanchk2(press)




def interpolate(nch, w=10):
    st=nch[0][1][0] -w
    en=nch[0][1][0]
    np.interp(nch[0][1][0] )
    
    
   





from sklearn.preprocessing import MinMaxScaler
def scalecomp(lst,m):
 
    return([m*(round(x-min(lst))) for x in lst])

    #return([x/max(mal) for x in lst])
   
    
    
   

#def interpo():
    

#def reclst(lst, ):
        
    
#    for index, item in enumerate(lst):
#    
#        if isinstance(lst[i], (target)) == False:
#            print('false')
#        
#        else 


            
#ranges = []
#subr=[]
#for i, item in enumerate(nans):
#    
#    
#    if i!=len(nans) - 1:
#
#        if nans[i+1]==item + 1:
#            subr.append(nans[i])        
#    else: subr.append(i) ; ranges.append(subr) 
#from itertools import groupby
#def ranges(lst):
#    pos = (j - i for i, j in enumerate(lst))
#    t = 0
#    for i, els in groupby(pos):
#        l = len(list(els))
#        el = lst[t]
#        t += l
#        yield range(el, el+l)


#y[nans]= np.interp(x(nans), x(~nans), y[~nans])