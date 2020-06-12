#!/usr/bin/env python
# coding: utf-8

# In[14]:


import turtle as t
t.shape('turtle')
t.fd(200)
t.fd(200)
t.left(90)
t.fd(200)
t.left(90)
t.fd(200)
t.fd(200)
t.left(90)
t.fd(200)
t.exitonclick()


# In[84]:


import turtle as t
t.shape('turtle')
t.color('red', 'yellow')
t.begin_fill()
t.fd(200)
t.fd(200)
t.left(130)
t.fd(200)
t.fd(90)
t.left(95)
t.fd(300)
t.end_fill()
t.exitonclick()


# In[86]:


from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()


# In[113]:


import turtle as t
t.shape('turtle')
t.color('red', 'yellow')
t.begin_fill()
t.rt(120)
t.fd(100)
t.fd(100)
t.left(120)
t.fd(200)
t.left(130)
t.fd(300)
t.rt(200)
t.fd(300)
t.left(160)
t.fd(240)
t.end_fill()
t.exitonclick()


# In[2]:


import turtle as t
t.shape('turtle')
t.color('red', 'yellow')
t.begin_fill()

n = int(input('몇각형???'))

for i in range(n):
    for i in range(n):
        t.fd(10)
        t.left(360/n)
    t.right(180/n)
t.end_fill()
t.exitonclick()

