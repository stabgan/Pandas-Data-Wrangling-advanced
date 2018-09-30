#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import copy


# In[73]:


l=[]
c = 0
for i in range(16,32) :
    print(i)
    x = pd.read_csv('2017-01-'+str(i)+'.csv', encoding='iso-8859-1' , sep = ';' ,header = 1)
    
    wd = pd.read_excel('weather-india.xlsx')
    wd = wd.iloc[::15].drop('Timestamp' , axis=1).reset_index().drop('index',axis=1)
    wd = wd.loc[c:c+97]
    c += 97
    wd = wd.reset_index()
    wd = wd.shift(3)

    wd.iloc[1] = wd.iloc[1].replace(np.nan , 'x')
    wd.iloc[0] = wd.iloc[0].replace(np.nan , 'x')
    wd.iloc[2] = wd.iloc[2].replace(np.nan , 'x')


    
    new = pd.concat([x,wd], axis=1)
    
    l.append(new)


# In[75]:


l[9]


# In[77]:


c = 16
for i in l :
    i.to_csv('data'+str(c)+'th', sep='\t', encoding='utf-8')
    c += 1


# In[78]:


d = pd.read_csv('data20th' , sep='\t')


# In[79]:


d


# In[ ]:




