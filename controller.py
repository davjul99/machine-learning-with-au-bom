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



url='http://www.bom.gov.au/fwo/IDN60801/IDN60801.94599.json'
sites = ['http://www.bom.gov.au/fwo/IDN60801/IDN60801.94599.json']
paraLst = ['air_temp', 'aifstime_utc' ]
#paraLst = ['air_temp' ]
url = 'http://www.bom.gov.au/fwo/IDN60801/IDN60801.'
sites = [url+'94596.json', url+'94599.json' ] 
#sites=[url+'94596.json', url+'94599.json', url+'94573.json', url+'94592.json', url+'94598.json', url+'95571.json', url + '95570.json', url + '94572.json' ] 

data = []
locData = {}
ss = StandardScaler()
mm=MinMaxScaler()
def getJdata(url):
   
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)

sdata= getJdata(sites[0])
wdata=sdata['observations']['data']




def getParamDict(dom, param):
    return(dom[param])
    
    
#wu =getJdata('http://api.wunderground.com/api/da1af438cabc981f/conditions/q/CA/San_Francisco.json')
def bldata(sites):
    
    for site in sites:
       
        pdict={}
        jsn= getJdata(site)
        js=jsn['observations']['data']
        
        for para in paraLst:
            for j in js:            
                data.append(j[para])
            pdict[para] = data
        locData[j['name']] = pdict    


def getParaData(para):    
    d=[]
    for w in wdata:
        d.append(w[para])
    return(d)
    

       
def getSiteData(paraLst):
    d=[]    
    for para in paraLst:
        d.append(getParaData(para))
    return(d)
            
na=np.array(getSiteData(paraLst))

def makeDf(data, labels):
    return(pd.DataFrame(data, labels))
   
#d=getSiteData(paraLst)
#bldata(sites)
