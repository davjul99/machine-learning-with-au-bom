# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 11:11:39 2017

@author: Home
"""



#url= 'http://www.bom.gov.au/fwo/IDN60801/IDN60801.94596.json'
#html = urllib.request.urlopen(url).read()
#js= json.dumps(html)

#import json,urllib
#data = urllib.request.urlopen("https://api.github.com/users?since=100").read()
#output = json.loads(str(data))
#print (output)

try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

import json
import matplotlib.pyplot as plt
#from datetime import datetime
#from dateutil.parser import parse
#import pandas as pd

def get_jsonparsed_data(url):
   
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)

       #"address=googleplex&sensor=false")
url = 'http://www.bom.gov.au/fwo/IDN60801/IDN60801.'
sites = [url+'94596.json', url+'94599.json' ] 
#sites=[url+'94596.json', url+'94599.json', url+'94573.json', url+'94592.json', url+'94598.json', url+'95571.json', url + '95570.json', url + '94572.json' ]      
#url=('http://www.bom.gov.au/fwo/IDN60801/IDN60801.94599.json')       



for site in sites:
    jsn= get_jsonparsed_data(site)
    js=jsn['observations']['data']
    rain=[0]
    time=[]
    temp=[]
    cloudBase=[]
    dewpt=[]
    apparent_t=[]
    rel_hum=[]
    wind_spd_kmh=[]
    
    parvar=rain
    
    for i, j in enumerate(js):
        try :
            rain.append(float(j['rain_trace']))
        except :            
            rain.append(None)
        try:
            dewpt.append(float(['dewpt']))
        except:
            dewpt.append(0)
        try:
            cloudBase.append(j['cloud_base_m'])
        except:
            cloudBase.append('')
            
        time.append(j['aifstime_utc'])
        temp.append(j['air_temp'])
        apparent_t.append(j['apparent_t'])
        rel_hum.append(float(j['rel_hum'])/2.5)
        wind_spd_kmh.append(float(j['wind_spd_kmh']))
        
        #print(cloudBase[i])
    #rate=[abs(x - rain[i-1]) for i, x in enumerate(rain) if i > 0] 
    cbscale=[]    
   
    for x in enumerate(cloudBase):
        try:cbscale.append((cloudBase[i] - min(x))/50)
        except: cbscale.append(-1)
        
    #cbScale = [try:int(x) - (cloudBase[i])/50 except: 0 for x in enumerate(cloudBase) ]    
#    rate=[abs(x - rain[i - 1]) for i, x in enumerate(rain) if i > 0] 
#    print(js[0]['name'])
#    print(time[0] +'\n')
#    print(time[len(time)-1])

    import random
    
    plt.title(j['name']) 
    plt.legend(handles=[])
    plt.xlabel('Time in hours from ' + time[0] + ' to ' + time[len(time)-1])
    #plt.plot(rate[218:0:-1])
    plt.plot(temp[0:218], label='Air Temp')
    plt.plot(apparent_t[0:218] ,label='Apparent Temp')
    plt.plot(rel_hum[0:218], label='Humidity/2.5')
    plt.plot(wind_spd_kmh[0:218], label='wind kmh')
    plt.plot(rain[0:218], label='rain')
    plt.plot(cbscale[0:218], label='cloudb')
    plt.axis([0,48,0,40])
    plt.grid()
    #plt.plot(dewpt[218:0:-1])
    
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    figname=str(j['name']) +str(time[0])
    plt.savefig(figname +'.png')
    plt.show()
#plt.axis([time[0], time[216]])
    
def scale(l ):
    mi=min(l)
    ma=max(l)
    ra=ma-mi
    sl=[]
    for i in l:
        sl.append((i-mi)/50)
        
    return sl

def getParameter(params): 
    return(params)