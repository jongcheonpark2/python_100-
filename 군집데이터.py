#!/usr/bin/env python
# coding: utf-8

# ### boolean

# In[8]:


True == False


# In[2]:


True != 0


# In[3]:


False == 0


# In[4]:


True or False


# In[5]:


1 =='1'


# ### 창의예제1

# In[6]:


False == True


# In[8]:


True == 0


# In[14]:


False != 2


# In[17]:


False or True


# In[18]:


1 =='2'Y


# ### 문자열

# In[10]:


eng = 'Korea COVID 19'
eng.lower()
eng.upper()


# ### Lists

# In[13]:


data = []
data.append('java')
data[0], data[-1], data[1:], data[:2]
data.sort()
data.reverse()


# ### Tuple

# In[9]:


b=(1,2,3, '사','오')


# In[10]:


c=1,2,3


# In[11]:


type(b), type(c)


# In[1]:


b[3] = 4


# In[13]:


b[3:], b[1:4]


# In[4]:


dic = {'name1' : '종천','학번1':30106, 'name2' :'종천2', '학번2':30107}
dic.get('name1')
dic.keys()
dic.values()


# ### set

# In[19]:


junch = {'햄버거', '치킨', '라면', '콜라', 10000}
dinner = {'피자','족발','라면','콜라', 10000}


# In[20]:


import pandas as pd


# In[21]:


li = [1,2,3]
li


# In[24]:


type(li)


# In[28]:


s1=pd.core.series.Series(li)
s1


# In[34]:


s2=pd.core.series.Series(['일','이','삼'])
s2


# In[36]:


pd.DataFrame(data)


# In[45]:


data=pd.DataFrame([['a',100],['b',200],['c',300]])
data.info()


# In[46]:


data.tail(1)


# In[47]:


data.tail(2)


# In[49]:


col=['1군','2군']


# In[55]:


pd.DataFrame([['a',100],['b',200],['c',300]],columns=col)


# In[59]:


man=[
    {'Name':'은주','Age':20, 'Job':'J1'},
    {'Name':'소주','Age':30, 'Job':'J2'},
    {'Name':'대주','Age':40, 'Job':'J3'},
]
pd.DataFrame(man, index=[1,2,3])


# In[63]:


a=[1,2,3]
b=[4,5,6]
df = [a, b]
dd=pd.DataFrame(df, index=[1,2], columns=['A','B','C'])
dd


# In[33]:


data=dict(num=s1, word=s2)
data


# In[31]:


pd.DataFrame()

