#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd


# In[7]:


df = pd.read_csv('weather.csv')


# In[8]:


df.head(3)


# In[9]:


df.tail(10)


# In[10]:


df.columns


# In[23]:


df = df[['年月日', '平均気温(℃)', '最高気温(℃)', '最低気温(℃)', '降水量の合計(mm)','最深積雪(cm)','平均雲量(10分比)', '平均蒸気圧(hPa)', '平均風速(m/s)','日照時間(時間)']][1:]


# In[25]:


df.dtypes


# In[26]:


df.shape


# In[27]:


df.index


# In[28]:


df.columns


# In[30]:


df.iloc[4:9,2:6]


# In[32]:


df_people = pd.read_csv('people.csv')
df_people


# In[41]:


df_people[df_people['nationality']=='America']


# In[44]:


df_people[(df_people['age'] < 30) & (df_people['age']<=20)]


# In[47]:


df_people['age'].unique()


# In[51]:


df_people['id'].unique()


# In[50]:


df_people['name'].unique()


# In[52]:


df_people['nationality'].unique()


# In[56]:


df_people.drop_duplicates(subset = 'nationality')


# In[ ]:


df

