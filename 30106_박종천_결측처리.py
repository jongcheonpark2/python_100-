#!/usr/bin/env python
# coding: utf-8

# ### 문제1. 엑셀파일을 가져올 수 있는가?

# In[5]:


import pandas as pd


# In[17]:


path ='covid1.csv'


# In[18]:


df=pd.read_csv(path)


# In[25]:


df


# ### 문제2. 결측열만 볼 수 있는가?

# In[98]:


null_count=df.isnull().sum()


# In[99]:


null_count


# In[100]:


df_null_count = null_count.reset_index()


# In[101]:


df_null_count.columns=['메뉴','결측']


# In[102]:


df_null_count


# In[103]:


df_null_count_3 = df_null_count.sort_values(by='결측',ascending=False).head(3)


# In[104]:


df_null_count_3


# In[105]:


drop_columns = df_null_count_3['메뉴']


# In[106]:


drop_columns


# In[107]:


drop_columns.to_list()


# In[108]:


df[drop_columns]


# In[109]:


print(df.shape)


# In[110]:


print(df.shape)


# In[111]:


df.head()


# In[117]:


df.info()


# ### 문제3. 결측열 제거하기

# In[115]:


df=df.drop(drop_columns, axis=1)

