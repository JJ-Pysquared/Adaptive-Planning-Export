import requests
import xmltodict
import pandas as pd
import numpy as np

#Adaptive API Methods: https://knowledge.adaptiveplanning.com/Integration/Managing_Data_Integration/API_Documentation/Understanding_the_Adaptive_Insights_API/API_Methods
# xml is what you will replace with your desired method from the above Adaptive Method API

xml = """<?xml version='1.0' encoding='UTF-8'?>
<call method="exportData" callerName="a string that identifies your client application">
<credentials login="Useremail@tenant.org" password="Password123" instanceCode="Instancename"/>
<version name="FY20 Budget" isDefault="false"/>
<format useInternalCodes="true" includeUnmappedItems="true"/>
<filters>
   <timeSpan start="00/0000" end="99/9999"/>
</filters>
<rules includeZeroRows="true" includeRollups="true" markInvalidValues="true" markBlanks="false" timeRollups="false">
   <currency useCorporate="false" useLocal="false" override="USD"/>
</rules>
</call>
"""
headers = {"headers":'headers'} # set what your server accepts
req= (requests.get('https://api.adaptiveinsights.com/api/v20', data=xml, headers=headers).text)

#Everything above is basically required the below is used to loop through your response and saving it to a csv

doc = xmltodict.parse(req)
splt=doc['response']['output'].split("\n")

df=pd.DataFrame(columns=[splt[0].split(',')])

num=1
for x in splt: 
    df.loc[num]=x
    num+=1

#will not run if you already have a document named Document.csv,if you run this you must delete the file every time 
df.to_csv('Document.csv',index = None, header=True)
print("Export is Done")
