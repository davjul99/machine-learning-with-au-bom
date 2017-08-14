# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 20:19:42 2017

@author: Home
"""

from urllib.request import urlopen
import json
import os
import pandas as pd
import numpy as np

class dataUte(object):
    data =[]
   
    
    def __init__(self, paraList, name, url):
        self.paraList = paraList
        self.name = name
        self.url = url
        
    def fetchData(self):
        
        response = urlopen(url)
        data = response.read().decode("utf-8")
        return json.loads(data)
        
        
    def getObsData(self):
        jsn= self.fetchData()
        return(jsn['observations']['data'])
            
    def getParaData(self, para):
            
        dl=[]
        od=self.getObsData()
        for d in od:
            dl.append(d[para])
        return(d)
        
    def getData(self, paraLst):
        d=[]    
        for para in paraLst:
            d.append(self.getParaData(para))
        #return(np.array(d))            
        return(d)
    
    def getSiteData(paraLst):
        d=[]    
        for para in paraLst:
            d.append(self.getParaData(para))
        return(d)

paraLst = ['air_temp', 'aifstime_utc' ]
url='http://www.bom.gov.au/fwo/IDN60801/IDN60801.94599.json'
d= dataUte(paraLst, 'Ballina', url)