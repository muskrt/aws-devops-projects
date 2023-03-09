#!/usr/bin/env python
# coding: utf-8

# In[9]:


import os 
import sys
import pandas as pd 
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt


# In[10]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[11]:


df =pd.read_csv('test.csv')


# In[12]:


df.head()


# In[13]:


df.info()


# In[14]:


df.fillna(-99999,inplace=True)


# In[15]:


xpoints=np.array(df['x'])
ypoints=np.array(df['y'])


# In[20]:


plt.plot(xpoints,ypoints,'o')
plt.show()


# In[27]:


x_train,x_test,y_train,y_test=train_test_split(df['x'],df['y'])


# In[31]:


plt.scatter(x_train,y_train,label="Train Data",color='r',alpha=.7)
plt.scatter(x_test,y_test,label="test Data",color='g',alpha=.7)
plt.legend()
plt.title('test train split')
plt.show()


# In[33]:


LR=LinearRegression()
LR.fit(x_train.values.reshape(-1,1),y_train.values)


# In[35]:


prediction=LR.predict(x_test.values.reshape(-1,1))
plt.plot(x_test,prediction,label='lineer regression',color='b')
plt.scatter(x_test,y_test,label='actual test data',color='g',alpha=0.7)
plt.legend()
plt.show()


# In[ ]:




