# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 10:16:09 2017

@author: Home
"""
from urllib.request import urlopen
import json
import os
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import matplotlib.pyplot as plt


url='http://www.bom.gov.au/fwo/IDN60801/IDN60801.94599.json'
paraLst = ['air_temp', 'aifstime_utc' ]


class dataUte(object):
    data =[]
    siteData=[]
   
    
    def __init__(self, paraList, name, url):
        self.paraList = paraList
        self.name = name
        self.url = url
        self.jdata=self.loadJson(url)

    def loadJson(self, url):
       
        response = urlopen(url)
        data = response.read().decode("utf-8")
        return(json.loads(data))
    
    def getObsData(self):

        #sdata= self.loadJson(url)
        
        return(self.jdata['observations']['data'])
 
    def getParaData(self,para):    
        d=[]
        obs=self.getObsData()
        for ob in obs:
            d.append(float(ob[para]))
        return(d)
                   
    def getSiteData(self,paraLst):
        d=[]    
        for para in paraLst:
            d.append(self.getParaData(para))
        return(d)
    
    
    
    def getParamDict(dom, param):
        return(dom[param])
        
    #na=np.array(getSiteData(paraLst))
    
    def makeDf(data, labels):
        return(pd.DataFrame(data, labels))


    def plotData(self, y):
        y=self.getSiteData(['air_temp'])
        x=self.getSiteData(['aifstime_utc'])
        for i in self.paraList:
            self.getSiteData
            y=y[0][0:218]
        #x=x[0][:]
        plt.axis([0,48,0,40])
        plt.grid()
        plt.plot(y)
        plt.show()
        
        
        
        
       
    #d=getSiteData(paraLst)
    #bldata(sites)
#paraLst = ['air_temp', 'aifstime_utc' ]
paraLst = ['air_temp', 'wind_spd_kmh', 'rel_hum' ]
url='http://www.bom.gov.au/fwo/IDN60801/IDN60801.94599.json'
d= dataUte(paraLst, 'Ballina', url)



from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import Imputer
import random

obs=d.getSiteData(paraLst)
obsT=obs

pf=PolynomialFeatures()


import numpy as np



def contImp(lst):
    for i, item in enumerate(lst):
        if isinstance(item, (int, float, complex, bool)) == True:
            return lst
        if i == len(lst)-1:
            return lst
        else:
            lst[i] = abs(lst[i-1]/lst[i+1])
            
            
            

