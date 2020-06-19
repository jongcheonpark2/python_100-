#!/usr/bin/env python
# coding: utf-8

# ### 여러개의 파일 가져오기

# In[78]:


import pandas as pd


# In[79]:


path=r'C:\Users\user\Desktop\301\score\A.csv'


# In[80]:


path


# In[81]:


pd.read_csv(path, encoding='cp949')


# In[82]:


path=r'C:\Users\user\Desktop\301\score\B.csv'


# In[83]:


path


# In[84]:


pd.read_csv(path, encoding='cp949')


# In[85]:


import glob


# In[86]:


data=r'C:\Users\user\Desktop\301\score\\' 


# In[105]:


stu=[]
for file in glob.glob(data+'*.csv'):
     data_stu =pd.read_csv(file, encoding='cp949') 
    stu.append(data_stu)


# In[89]:


a=[]


# In[91]:


a


# In[92]:


a.append(3)


# In[93]:


a


# In[94]:


a.append(10)


# In[95]:


a


# In[96]:


stu=[]


# In[97]:


stu


# In[103]:


data_stu =pd.read_csv(file, encoding='cp949')
stu.append(file

