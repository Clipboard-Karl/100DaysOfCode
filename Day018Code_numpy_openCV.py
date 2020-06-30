#100DaysOfCode 017/100 - Working with panda
#   2020-06-28
#
#  I wanted to finish the pandas section to start fresh with a new section in
#     the morning.
#
#  The following was generated with jupyter notebook

#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
os.listdir()


# In[4]:


import pandas


# In[5]:


df4=pandas.read_csv("supermarkets-commas.txt")
df4


# In[40]:


df7 = df4.drop("City",1)  # 1 is for dropping a column
df7.set_index("Address", inplace = True)
df7 = df7.drop("332 Hill St",0)
df7


# In[42]:


# shape appeares to have been dropped or my lesson is outdated in some other way
#df7 = df4["Contient"]["1","2","3","4","5"]
df7_t=df7.T
df7_t


# In[46]:


df7_t["My Address"]=[1,"My State","My Country","Me",22]
df7_t


# In[50]:


df7=df7_t.T
df7


# In[51]:


dfkarl=df4
dfkarl


# In[52]:


#   for the next step I used "pip3 install geopy"
import geopy
dir(geopy)


# In[57]:


from geopy.geocoders import ArcGIS
nom=ArcGIS()


# In[66]:


nom.geocode("1554 Newville Rd, Carlisle, PA 17015")


# In[61]:


n=nom.geocode("1554 Newville Rd, Carlisle, PA 17015")
print(n)


# In[64]:


n.latitude


# In[65]:


n.longitude


# In[67]:


type(n)


# In[68]:


dfgeorge=pandas.read_csv("supermarkets.csv")
dfgeorge


# In[71]:


dfgeorge["Address"]=dfgeorge["Address"]+", "+dfgeorge["City"]+", "+dfgeorge["State"]+", "+dfgeorge["Country"]
dfgeorge


# In[83]:


dfgeorge["Coordinates"]=dfgeorge["Address"].apply(nom.geocode)
dfgeorge.Coordinates


# In[75]:


dfgeorge.Coordinates[0]


# In[76]:


dfgeorge.Coordinates[0].latitude


# In[84]:


dfgeorge


# In[88]:


dfgeorge["Latitude"]=dfgeorge["Coordinates"].apply(lambda x:x.latitude if x != None else None)
dfgeorge["Longitude"]=dfgeorge["Coordinates"].apply(lambda x:x.longitude if x != None else None)
dfgeorge
