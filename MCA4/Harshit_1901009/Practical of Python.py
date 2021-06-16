#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import pandas_profiling as pp


# In[2]:


df=pd.read_csv("station_day.csv")
df.head()


# In[3]:


df=df.loc[df.StationId=='DL005']
df.head()


# In[4]:


df.info()


# In[5]:


pp.ProfileReport(df)


# In[6]:


df.describe()


# In[7]:


df.drop(['Xylene'],axis=1,inplace=True)
df


# In[8]:


df.fillna(0)
df


# In[9]:


df1=df[['PM10','NO','SO2','O3']]
df1.hist()


# In[14]:


df[10:21]


# In[ ]:




