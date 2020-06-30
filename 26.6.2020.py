#!/usr/bin/env python
# coding: utf-8

# In[23]:


import pandas
dfs = pandas.read_html('https://rate.bot.com.tw/cr?Lang=zh-TW')


# In[17]:


type(dfs)


# In[8]:


dfs[0]


# In[9]:


money = dfs[0]
type(money)


# In[14]:


money.ix [:,0:2]


# In[18]:


dfs[0]


# In[20]:


money.ix[:,0:2]


# In[ ]:




