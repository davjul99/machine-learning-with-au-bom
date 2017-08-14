# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 10:16:09 2017

@author: Home
"""
from urllib.request import urlopen
import json

import pandas as pd
from sklearn.pipeline import Pipeline
import sklearn.preprocessing as pre 
#from sklearn.preprocessing import StandardScaler as ss
import numpy as np
import matplotlib.pyplot as plt


url='http://www.bom.gov.au/fwo/IDN60801/IDN60801.94599.json'
paraLst = ['air_temp', 'aifstime_utc' ]


class dataUte(object):
    #data =[]
    #siteData=[]
   
    
    def __init__(self, paraList, name, url):
        self.paraList = paraList
        self.name = name
        self.url = url
        self.jdata=self.loadJson(url)
        self.obsDat=self.jdata['observations']['data']

    def loadJson(self, url):
       
        response = urlopen(url)
        data = response.read().decode("utf-8")
        return(json.loads(data))
    
    def getObsData(self):
        #sdata= self.loadJson(url)        
        #return(self.jdata['observations']['data'])
        return(self.obsDat)
 
    def getParaData(self,para):    
        d=[]
        #obs=self.getObsData()
        for ob in self.obsDat:
            d.append(float(ob[para]))
        return(d)
                   
    def getSiteData(self):
        d=[]    
        for para in self.paraList:
            d.append(self.getParaData(para))
        return(d)
    
    
    def makeDf(data, labels):
        return(pd.DataFrame(data, labels))

    def scaleDat(self, lst):
        
        sd = np.array(lst)
        ssd = pre.scale(sd)
        return(ssd)


    def plotData(self):
        for para in self.paraList:
            p =self.getParaData(para)
            plt.plot(self.scaleDat(p), label=str(para))
            #plt.plot(p, label=str(para))
        
        #x=x[0][:]
        plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
        plt.axis([0,48,-2,2])
        #
        #plt.axis([0,48,0,40])
        plt.grid()
        #plt.plot(y)
        plt.show()
    
        
 
       
    #d=getSiteData(paraLst)
    #bldata(sites)
#paraLst = ['air_temp', 'aifstime_utc' ]
paraLst = ['air_temp', 'wind_spd_kmh', 'rel_hum' ]
url='http://www.bom.gov.au/fwo/IDN60801/IDN60801.94599.json'
url2='http://www.bom.gov.au/fwo/IDN60801/IDN60801.94598.json'
d= dataUte(paraLst, 'Ballina', url)
d2=dataUte(paraLst, 'erm', url2)


#sites=[url+'94596.json', url+'94599.json', url+'94573.json', url+'94592.json', url+'94598.json', url+'95571.json', url + '95570.json', url + '94572.json' ]

sites=[url+'94596.json']


#sd=np.array(d.getSiteData(['air_temp','press','rel_hum' ]))

#from sklearn.ensemble import RandomForestRegressor
#
#rfr=RandomForestRegressor()
#sdy=np.array(d2.getSiteData(['air_temp','press']))
#res=rfr.fit_transform(sd.transpose(), sdy.transpose())
#
#ssd = StandardScaler().fit_transform(sd.transpose())
#ssdy = StandardScaler().fit_transform(sdy.transpose())
#res=rfr.fit_transform(ssd, ssdy)
#plt.plot(res)
#
#
#
#
#
#
################################################################
#
#
#
#
#from sklearn.preprocessing import PolynomialFeatures
#from sklearn.preprocessing import Imputer
#import random
#
##obs=d.getSiteData(paraLst)
##obsT=obs
#
#pf=PolynomialFeatures()
#
#
#import numpy as np
#
#
#
#def contImp(lst):
#    for i, item in enumerate(lst):
#        if isinstance(item, (int, float, complex, bool)) == True:
#            return lst
#        if i == len(lst)-1:
#            return lst
#        else:
#            lst[i] = abs(lst[i-1]/lst[i+1])
#            
#            
#            
#
