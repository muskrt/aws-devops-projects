#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


# In[4]:


d = {'col1': [1, 2], 'col2': [3, 4]}
df = pd.DataFrame(data=d)


# In[ ]:


df.head()


# In[ ]:


df=pd.read_csv('test.csv')


# In[ ]:


df.head(10)


# In[47]:


sql_table="Data"
sql_create_table=pd.io.sql.get_schema(df,name=sql_table)
print(sql_create_table)


# In[73]:


file=open("dataframe.sql",'a')
file.write(sql_create_table+";\n")
file.close()
file=open("dataframe.sql",'a')
for i in range(0,300):
    sql_cmd=""" INSERT INTO {SQL_TABLE} VALUES ({X},{Y})""".format(SQL_TABLE=sql_table,X=df['x'][i],Y=df['y'][i])+";\n"
    file.write(sql_cmd)
file.close()
    


# In[37]:


df.head(5)


# In[74]:


df.info()

